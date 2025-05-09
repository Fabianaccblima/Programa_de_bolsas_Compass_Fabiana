from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf, rand, floor
import random

# Criando a sessão do Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Análise de Nomes") \
    .getOrCreate()

# Lendo o arquivo de texto com nomes de pessoas
nome_dos_dados = spark.read.csv("/home/fabiana/nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeando a coluna para 'NomePessoa'
nome_dos_dados = nome_dos_dados.withColumnRenamed('_c0', 'NomePessoa')

# Exibindo o schema do DataFrame para verificação
nome_dos_dados.printSchema()

# Exibindo as primeiras 10 entradas do DataFrame
nome_dos_dados.show(10)

# Adicionando a coluna de nível educacional
def obter_nivel_educacional():
    return random.choice(["Ensino Fundamental", "Ensino Médio", "Ensino Superior"])

# Registrando a UDF para o nível educacional
udf_nivel_educacional = udf(obter_nivel_educacional, StringType())

# Adicionando a coluna "Nível Educacional"
nome_dos_dados = nome_dos_dados.withColumn("NivelEducacional", udf_nivel_educacional())

# Adicionando a coluna de País de Origem

lista_paises = ["Suriname", "Argentina", "Peru", "Brasil", "Guiana", 
                "Uruguai", "Colômbia", "Bolívia", "Equador", "Guyana", 
                "Venezuela", "Paraguai", "Chile"]

# Função para selecionar um país aleatório
def selecionar_pais():
    return random.choice(lista_paises)

# Registrando a UDF para país de origem
udf_pais_origem = udf(selecionar_pais, StringType())

# Adicionando a coluna País de Origem"
nome_dos_dados = nome_dos_dados.withColumn("PaisOrigem", udf_pais_origem())


# Gerando um ano aleatório entre 1945 e 2010
nome_dos_dados = nome_dos_dados.withColumn("AnoNascimento", (floor(rand() * (2010 - 1945 + 1)) + 1945))

# Filtrando pessoas nascidas a partir do ano 2000
dados_filtro_2000 = nome_dos_dados.select("*").filter(nome_dos_dados["AnoNascimento"] >= 2000)

# Exibindo as primeiras 10 linhas do DataFrame filtrado
dados_filtro_2000.show(10)

# Registrando o DataFrame como uma tabela temporária
nome_dos_dados.createOrReplaceTempView("tabela_pessoas")

# Executando a consulta SQL para selecionar pessoas nascidas a partir de 2000
spark.sql("SELECT * FROM tabela_pessoas WHERE AnoNascimento >= 2000").show()

# Contando o número de pessoas da geração Millennial (nascidos entre 1980 e 1994)
dados_millennials = nome_dos_dados.filter((nome_dos_dados["AnoNascimento"] >= 1980) & (nome_dos_dados["AnoNascimento"] <= 1994))

# Contando quantas pessoas da geração Millennials existem
quantidade_millennials = dados_millennials.count()
print(f"Total de pessoas da geração Millennials: {quantidade_millennials}")

# Repetindo a contagem de Millennials 
spark.sql("SELECT COUNT(*) AS total_millennials FROM tabela_pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").show()

# Definindo as faixas etárias para cada geração
faixa_etaria_geracoes = [
    ("Baby Boomers", 1944, 1964),
    ("Geração X", 1965, 1979),
    ("Millennials", 1980, 1994),
    ("Geração Z", 1995, 2015)
]

# Criando uma lista para armazenar os DataFrames de contagem por geração
resultados_geracoes = []

for nome_geracao, ano_inicio, ano_fim in faixa_etaria_geracoes:
    # Filtrando o DataFrame pela faixa etária
    df_geracao_atual = nome_dos_dados.filter((nome_dos_dados["AnoNascimento"] >= ano_inicio) & (nome_dos_dados["AnoNascimento"] <= ano_fim))
    
    # Contando o número de pessoas por país na faixa etária
    df_geracao_count = df_geracao_atual.groupBy("PaisOrigem").count().withColumn("Geracao", udf(lambda: nome_geracao, StringType())())
    
    resultados_geracoes.append(df_geracao_count)

# Unindo os DataFrames de todas as gerações
df_geracoes_unidas = resultados_geracoes[0]
for df_geracao in resultados_geracoes[1:]:
    df_geracoes_unidas = df_geracoes_unidas.union(df_geracao)

# Exibindo os resultados ordenados por país, geração e contagem
df_geracoes_unidas.orderBy("PaisOrigem", "Geracao", "count").show()
