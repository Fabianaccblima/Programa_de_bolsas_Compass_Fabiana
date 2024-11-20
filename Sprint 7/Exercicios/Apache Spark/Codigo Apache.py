from pyspark.sql.functions import explode, split
from pyspark.sql import SparkSession

# Cria uma SparkSession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Caminho do arquivo dentro do Docker
docker_file_path = "/home/jovyan/README.md"  # Caminho do arquivo no container Docker
# Caminho do arquivo no Docker (com 'file://' para garantir acesso ao sistema de arquivos local)
docker_file_path = "file:///home/jovyan/README.md"  # Caminho completo do arquivo no contêiner Docker

# Lê o arquivo diretamente do caminho no Docker
df = spark.read.text(docker_file_path)

# Processa os dados (contagem de palavras)
word_counts = df.select(explode(split(df.value, r"\s+")).alias("word")) \
    .groupBy("word") \
    .count() \
    .orderBy("count", ascending=False)

# Salva o resultado em um arquivo CSV dentro do Docker (com um arquivo de saída único)
word_counts.coalesce(1).write.option("header", "true").csv("/home/jovyan/word_counts_output.csv")

# Exibe a mensagem de sucesso
print("Contagem de palavras salva em '/home/jovyan/word_counts_output.csv'.")
