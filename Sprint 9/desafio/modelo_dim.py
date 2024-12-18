import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql import Window
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType  
import datetime

# Criando o contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Lendo os arquivos Parquet diretamente do bucket S3
csv_df = spark.read.option("header", "true").parquet("s3://data-lake-de-fabiana/trusted/csv/filmes/2024/12/06/")
tmdb_df = spark.read.option("header", "true").parquet("s3://data-lake-de-fabiana/trusted/tmdb/parquet/2024/12/06/")

# Renomeando colunas para evitar ambiguidades após o JOIN
csv_df = csv_df.withColumnRenamed("popularidade", "csv_popularidade")
tmdb_df = tmdb_df.withColumnRenamed("popularidade", "tmdb_popularidade")
tmdb_df = tmdb_df.withColumnRenamed("generos", "tmdb_generos")
csv_df = csv_df.withColumnRenamed("genero", "csv_genero")

# Realizando o JOIN
joined_df = csv_df.join(
    tmdb_df,
    (F.lower(F.trim(csv_df['titulopincipal'])) == F.lower(F.trim(tmdb_df['nome']))),
    'inner'
)

# Criando a coluna 'decada'
final_df = joined_df.withColumn(
    'decada',
    (F.floor(F.col('anoLancamento').cast('int') / 10) * 10)
)

# Filtrando para incluir apenas filmes que possuem "comédia" e "romance" em seus gêneros
filtered_df = final_df.filter(
    (F.lower(F.col('csv_genero')).contains('comedy')) & 
    (F.lower(F.col('csv_genero')).contains('romance')) &
    (F.col('anoLancamento').cast('int').between(1984, 2022))  # Filtrando os anos entre 1984 e 2022
)

# Criando uma janela para particionar por década e ordenar por nota média e popularidade
window_spec = Window.partitionBy("decada").orderBy(
    F.desc("notaMedia"), 
    F.desc("tmdb_popularidade")
)

# Adicionando a classificação de filmes por década
ranked_df = filtered_df.withColumn("rank", F.row_number().over(window_spec))

# Filtrando para pegar apenas os 3 filmes mais bem avaliados por década
top_filmes = ranked_df.filter(F.col("rank") <= 3)

# Criando a tabela de dimensão de filmes (id, nome, e duração)
dim_filmes = top_filmes.filter(F.col('runtime') != 0).select(
    F.col('titulopincipal').alias('titulo'),
    F.col('runtime').alias('duracao')
).dropDuplicates(['titulo'])

# Adicionando uma chave artificial para a dimensão de filmes
dim_filmes = dim_filmes.withColumn("dim_filme_id", F.monotonically_increasing_id())

# Criando a tabela de dimensão de genero e garantindo que 'comedy' e 'romance' sempre apareçam
def garantir_comedia_romance(generos):
    generos = generos.split(',')  
    if 'comedy' not in generos:
        generos.append('comedy')  
    if 'romance' not in generos:
        generos.append('romance')  
    return ','.join(generos)  

# Registrar a função como UDF
garantir_comedia_romance_udf = F.udf(garantir_comedia_romance, StringType())  

# Aplicando a UDF para garantir que 'comedy' e 'romance' estão sempre presentes
dim_genero = top_filmes.withColumn(
    'csv_genero', 
    garantir_comedia_romance_udf(F.col('csv_genero'))
)

# Dividindo a coluna 'csv_genero' em uma lista de gêneros
dim_genero = dim_genero.withColumn(
    'genero_lista', 
    F.split(F.col('csv_genero'), ',')  

# Explodindo a lista de gêneros para criar uma linha separada para cada gênero
dim_genero = dim_genero.withColumn(
    'genero', 
    F.explode(F.col('genero_lista'))  
)

# Remover duplicatas
dim_genero = dim_genero.select('genero').dropDuplicates()

# Adicionando ID único para a tabela de dimensão de gênero
dim_genero = dim_genero.withColumn(
    "dim_genero_id", F.monotonically_increasing_id()
)

# Criando a tabela de dimensão de tempo, convertendo 'ano' e 'decada' para inteiro
dim_tempo = top_filmes.select(
    F.col('anoLancamento').alias('ano')
).dropDuplicates().withColumn(
    'decada',
    (F.floor(F.col('ano').cast('int') / 10) * 10)
).withColumn("dim_tempo_id", F.monotonically_increasing_id()) \
   .withColumn('ano', F.col('ano').cast('int')) \
   .withColumn('decada', F.col('decada').cast('int'))

# Criando a tabela de fato de filmes e adicionando o campo id_fato
fato_filmes = top_filmes.join(dim_tempo, "decada").join(
    dim_filmes,
    (top_filmes['titulopincipal'] == dim_filmes['titulo']),
    "inner"
).join(
    dim_genero,
    (top_filmes['csv_genero'] == dim_genero['genero']),
    "inner"
).select(
    dim_tempo["dim_tempo_id"],
    dim_filmes["dim_filme_id"],
    dim_genero["dim_genero_id"],  
    F.col('tmdb_popularidade').alias('popularidade').cast('float'),
    F.col('notaMedia').alias('notaMedia').cast('float')
)

# Adicionando a chave primária id_fato na tabela de fato
fato_filmes = fato_filmes.withColumn("id_fato", F.monotonically_increasing_id())

# Obtendo a data atual no formato ano/mes/dia
current_date = datetime.datetime.now().strftime("%Y/%m/%d")

# Definindo os caminhos de saída com base na data atual
output_dim_filmes_path = f"s3://data-lake-de-fabiana/refined/dim_filmes/{current_date}/"
output_dim_tempo_path = f"s3://data-lake-de-fabiana/refined/dim_tempo/{current_date}/"
output_fato_filmes_path = f"s3://data-lake-de-fabiana/refined/fato_filmes/{current_date}/"
output_dim_genero_path = f"s3://data-lake-de-fabiana/refined/dim_genero/{current_date}/"  

# Salvando as tabelas de dimensões e a tabela de fato em formato Parquet
dim_filmes.write.mode("overwrite").parquet(output_dim_filmes_path)
dim_tempo.write.mode("overwrite").parquet(output_dim_tempo_path)
fato_filmes.write.mode("overwrite").parquet(output_fato_filmes_path)
dim_genero.write.mode("overwrite").parquet(output_dim_genero_path)  

print(f"Tabelas de dimensões e fato salvas com sucesso em {current_date}.")
