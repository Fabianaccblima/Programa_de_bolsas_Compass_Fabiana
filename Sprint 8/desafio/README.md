## Análise 

Resumo da Análise:

Objetivo:

Analisar a evolução dos filmes de comédia romântica de 1984 a 2022, investigando a relação entre nota média, popularidade, e duração. O foco é entender como o tempo de duração e a recepção crítica (nota média, popularidade) influenciam o desempenho dos filmes ao longo das décadas.

#### Principais Áreas de Análise:

#### Evolução da Nota Média por Década:
Como as avaliações críticas dos filmes de comédia romântica mudaram ao longo do tempo (1984 a 2022).

#### Impacto da Duração no Desempenho:
Análise da relação entre a duração do filme (tempo de duração) e a nota média. Será investigado se há uma correlação entre filmes mais curtos ou mais longos e as avaliações críticas dos filmes.

#### Popularidade e Nota Média:
Como a popularidade de um filme afeta sua avaliação crítica (nota média). Filmes mais populares recebem notas mais altas ou baixas? Existe algum padrão ao longo das décadas?

#### Produção de Filmes por Década:
Quantidade de filmes de comédia romântica lançados em cada década e análise das tendências de popularidade dentro do gênero.

#### Objetivo Final:
Identificar padrões e fatores que influenciam o sucesso de filmes de comédia romântica, considerando tanto a recepção crítica quanto a popularidade dos filmes ao longo do tempo. A análise vai explorar se a duração dos filmes tem um papel significativo em seu desempenho em termos de crítica e popularidade, além de examinar as mudanças nas tendências de produção e recepção do gênero por década.

## Criar um job AWS GLUE

1- Criei um job chamado `sprint8` em um script Spark no editor do AWS Glue para acessar e processar meu arquivo .csv na camada Raw do S3. O job transformou os dados em formato Parquet e os armazenou na camada Trusted, garantindo que estivessem prontos para análise.

![alt text](../evidencias/job_sprint8.png)

## AWS IAM

Criei uma função no AWS IAM chamada `sprint8`  e configurei permissões com políticas como AmazonS3FullAccess, AmazonS3ReadOnlyAccess, AWSGlueConsoleFullAccess e AWSGlueServiceRole. Adicionei uma política em linha chamada ` desafiosprint8`  que permitiu acessar e manipular arquivos nas camadas Raw e de transformação no S3. Também autorizei ações no AWS Glue para gerenciar tabelas e bancos de dados específicos e para iniciar e monitorar o job DataProcessingJob.

![alt text](../evidencias/IAM.png)

## AWS Job Details

Fiz as seguintes configurações para o job no AWS Glue: selecionei a função IAM criada: sprint8. Defini o tipo como Spark. Para a versão do Glue, escolhi 3.0 e usei a linguagem Python 3.0. O tipo de worker foi configurado como Gx1 e solicitei 2 workers. Além disso, defini o tempo de execução do job como 60 minutos.

![alt text](../evidencias/jobdetails_sprint8.png)

## AWS Job Parameters

Nos parâmetros do job, defini o input como o local de origem dos dados que serão processados pelo job, e o target como o destino para onde os dados processados serão armazenados.

![alt text](../evidencias/jobparameters.png)


## Script csv (sprint8)

### 1 - Importei as bibliotecas: 

```
sys, datetime, awsglue.transforms, awsglue.utils, pyspark.context, awsglue.context, awsglue.job, awsglue.dynamicframe e pyspark.sql.functions.

```
Pois são bibliotecas essenciais para a execução de um job no AWS Glue, incluindo módulos para manipulação de argumentos (sys e awsglue.utils), gerenciamento de datas (datetime) e configuração do contexto Spark (pyspark.context e awsglue.context). Ele utiliza Job para controlar a execução do job e DynamicFrame para processar dados de forma flexível. Além disso, funções do pyspark.sql.functions como when, col, lower e trim são usadas para transformar os dados durante o processamento.

### 2 - Receber o nome do job e os caminhos S3

`args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])`

O código usa a função getResolvedOptions para obter os argumentos necessários ao job: o nome do job (JOB_NAME), o caminho do arquivo de entrada no S3 (S3_INPUT_PATH) e o destino no S3 para armazenar os dados processados (S3_TARGET_PATH).

### 3 - Inicializar o Glue Context e caminhos de entrada e saída 


```
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

```

O código inicializa o SparkContext e o GlueContext para gerenciar o job no AWS Glue, configurando a sessão Spark e o job com o nome definido em JOB_NAME. Os caminhos de entrada e saída fornecidos em S3_INPUT_PATH e S3_TARGET_PATH são atribuídos às variáveis source_file e target_path para processamento.

### 4 - Ler o arquivo CSV como DynamicFrame e converte para Dataframe

```
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

# Converter o DynamicFrame para DataFrame para transformações
raw_data = df.toDF()

```
O código lê o arquivo CSV do S3 a partir de source_file como um DynamicFrame, configurando o formato com cabeçalho e separador |. Depois, converte o DynamicFrame para um DataFrame Spark em raw_data, permitindo as transformações.

### 5 - Tratamento e Normalização

```
# Substitui zeros por null em todas as colunas
df_no_zeros = raw_data.select(
    [when(col(c) == 0, None).otherwise(col(c)).alias(c) for c in raw_data.columns]
)

# Normaliza as colunas de textos
for col_name in df_no_zeros.columns:
    if dict(df_no_zeros.dtypes)[col_name] == 'string':
        df_no_zeros = df_no_zeros.withColumn(col_name, trim(lower(col(col_name))))

# Remove as duplicatas
df_cleaned = df_no_zeros.dropDuplicates()

# Remove colunas de particionamento indesejadas
columns_to_remove = ['partition_0', 'partition_1', 'partition_2', 'partition_3']
df_cleaned = df_cleaned.drop(*columns_to_remove)

# Remove linhas com valores nulos (se necessário)
df_cleaned = df_cleaned.na.drop()

# Converte de volta para DynamicFrame
clean_data = DynamicFrame.fromDF(df_cleaned, glueContext, "clean_data")

```
O código começa normalizando as colunas de texto, aplicando a função trim e lower para remover espaços e converter o texto para minúsculas. Em seguida, remove duplicatas com dropDuplicates e exclui colunas de particionamento desnecessárias, como partition_0, partition_1, etc. Depois, elimina as linhas com valores nulos usando na.drop(). Por fim, converte o DataFrame limpo de volta para um DynamicFrame para ser usado no Glue.

### 6 - Obter data atual e contruir caminho de saída

```
# Obter a data atual para a estrutura de diretórios
current_date = datetime.now()
year = current_date.year
month = str(current_date.month).zfill(2)  
day = str(current_date.day).zfill(2)

# Construi o caminho de saída com a estrutura desejada
output_path = f"{target_path}/filmes/{year}/{month}/{day}"

```
O código obtém a data atual e formata o ano, mês e dia da execução. Em seguida, constrói o caminho de saída output_path, combinando o caminho de destino base target_path com o ano, mês e dia em que o processo foi executado.

### 7 - Salva os dados limpos em Parquet e finaliza o job

```
# Salva os dados limpos no formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=clean_data,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

# Finaliza o Job
job.commit()

```

O código salva os dados limpos no formato Parquet no caminho de saída especificado em output_path, usando o glueContext. Em seguida, finaliza a execução do job com o comando job.commit().

![alt text](../evidencias/job_sucesso.png)

## S3

Os arquivos CSV, após serem processados e convertidos para o formato Parquet, foram salvos na camada trusted do Data Lake.

![alt text](../evidencias/csv_s3.png)

![alt text](../evidencias/path_csv.png)


## Crawler

Criei um crawler chamado `csv_crawler` para explorar o caminho s3://data-lake-de-fabiana/trusted/csv/ na camada trusted do S3. Configurei o crawler para usar a IAM role `sprint8` e criei a base de dados `desafiosprint8` no Glue Data Catalog e o executei.

![alt text](../evidencias/crawler_csv.png)

![alt text](../evidencias/csv_crawler.png)

## Tabela

A tabela csv foi criada.

![alt text](../evidencias/table_csv.png)


## AWS Athena

![alt text](../evidencias/athena_csv.png)

![alt text](../evidencias/athena_csv_1.png)

![alt text](../evidencias/athena_aws_csv.png)


## Criar um job AWS GLUE