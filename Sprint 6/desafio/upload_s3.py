import boto3
from datetime import datetime  

# Credenciais AWS 
aws_access_key_id = 
aws_secret_access_key = 
aws_session_token = 

# Criar um cliente S3 com as credenciais temporárias
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name='us-east-1'  
)

# Nome do bucket e arquivos
bucket = 'data-lake-de-fabiana'  

# Lista de arquivos a serem enviados e suas especificações
arquivos = [
    '/app/movies.csv',
    '/app/series.csv'
]

# Nomes dos arquivos
nomes_arquivos = [
    'filmes.csv',  # Nome para o arquivo de filmes
    'series.csv'   # Nome para o arquivo de séries
]

# Obtendo a data atual para formatar o caminho
data_atual = datetime.now()
ano = data_atual.strftime('%Y')  # Ano
mes = data_atual.strftime('%m')  # Mês
dia = data_atual.strftime('%d')  # Dia

try:
    # Criar o bucket (ignorar se o bucket já existir)
    s3.create_bucket(Bucket=bucket)
    print(f'Bucket "{bucket}" criado com sucesso ou já existente.')

    # Iterar sobre os arquivos e fazer o upload
    for arquivo, nome_arquivo in zip(arquivos, nomes_arquivos):
        # Caminho no S3 com a estrutura especificada
        s3_path = f'raw/local/csv/{nome_arquivo[:-4]}/{ano}/{mes}/{dia}/{nome_arquivo}'  # Ajusta o caminho para o padrão
        # Fazer upload do arquivo para o bucket na pasta especificada
        s3.upload_file(arquivo, bucket, s3_path)
        print(f'Arquivo "{nome_arquivo}" enviado para o bucket "{bucket}" em "{s3_path}" com sucesso!')

except Exception as e:
    print(f'Ocorreu um erro: {e}')




