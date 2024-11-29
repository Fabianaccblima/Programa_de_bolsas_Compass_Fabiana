import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame  
from pyspark.sql.functions import when, col, lower, trim

# Recebe o nome do job e os caminhos S3
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

# Ler o arquivo CSV como DynamicFrame
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

# Converte o DynamicFrame para DataFrame para transformações
raw_data = df.toDF()

# Substitui zeros por null em todas as colunas
df_no_zeros = raw_data.select(
    [when(col(c) == 0, None).otherwise(col(c)).alias(c) for c in raw_data.columns]
)

# Normaliza as colunas de textos
for col_name in df_no_zeros.columns:
    if dict(df_no_zeros.dtypes)[col_name] == 'string':
        df_no_zeros = df_no_zeros.withColumn(col_name, trim(lower(col(col_name))))

# Remove duplicatas
df_cleaned = df_no_zeros.dropDuplicates()

# Remove colunas de particionamento indesejadas
columns_to_remove = ['partition_0', 'partition_1', 'partition_2', 'partition_3']
df_cleaned = df_cleaned.drop(*columns_to_remove)

# Remove linhas com valores nulos (se necessário)
df_cleaned = df_cleaned.na.drop()

# Converte de volta para DynamicFrame
clean_data = DynamicFrame.fromDF(df_cleaned, glueContext, "clean_data")

# Obter a data atual para a estrutura de diretórios
current_date = datetime.now()
year = current_date.year
month = str(current_date.month).zfill(2)  
day = str(current_date.day).zfill(2)

# Construi o caminho de saída com a estrutura desejada
output_path = f"{target_path}/filmes/{year}/{month}/{day}"

# Salva os dados limpos no formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=clean_data,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

# Finaliza o Job
job.commit()
