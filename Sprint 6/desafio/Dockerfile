FROM python

WORKDIR /app

# Copiando o script para o contêiner
COPY upload_s3.py /app/upload_s3.py
COPY movies.csv /app/movies.csv
COPY series.csv /app/series.csv

# Instalando dependências
RUN pip install boto3

# Comando para executar o script
CMD ["python", "upload_s3.py"]





