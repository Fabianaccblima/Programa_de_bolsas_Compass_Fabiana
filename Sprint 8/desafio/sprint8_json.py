import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_date, year, month, dayofmonth, explode, col

# Receber o nome do job e os caminhos S3
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Ler o arquivo JSON como DynamicFrame
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="json"
)

# Converte o DynamicFrame para DataFrame 
dataframe = df.toDF()

# Verifica o schema do DataFrame para garantir que todas as colunas estejam como desejado
dataframe.printSchema()

# Adicionar uma coluna 'data_criacao' com a data atual formatada como 'YYYY/MM/DD'
dataframe = dataframe.withColumn("data_criacao", current_date())

# Explodir a lista de filmes em várias linhas
dataframe_exploded = dataframe.withColumn("filme", explode(col("filmes_comedia_romance")))

# Seleciona e cria colunas individuais da estrutura interna de 'filme'
dataframe_normalized = dataframe_exploded.select(
    col("filme.nome").alias("nome"),
    col("filme.ano").alias("ano"),
    col("filme.popularidade").alias("popularidade"),
    col("filme.nota_media").alias("nota_media"),
    col("filme.votos").alias("votos"),
    col("filme.orcamento").alias("orcamento"),
    col("filme.receita").alias("receita"),
    col("filme.runtime").alias("runtime"),
    col("filme.generos").alias("generos"),
    col("data_criacao")
)

# Obtem valores de ano, mês e dia como strings para compor o caminho
year_value = dataframe_normalized.select(year(dataframe_normalized["data_criacao"])).distinct().collect()[0][0]
month_value = dataframe_normalized.select(month(dataframe_normalized["data_criacao"])).distinct().collect()[0][0]
day_value = dataframe_normalized.select(dayofmonth(dataframe_normalized["data_criacao"])).distinct().collect()[0][0]

# Montar o caminho final de saída 
output_path = f"{target_path}/parquet/{year_value:04d}/{month_value:02d}/{day_value:02d}"

# Salvar os dados em Parquet
dataframe_normalized.write.mode("overwrite").parquet(output_path)

# Finalizar o Job
job.commit()
