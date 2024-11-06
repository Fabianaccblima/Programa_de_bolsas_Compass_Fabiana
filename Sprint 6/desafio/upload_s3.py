import boto3
from datetime import datetime  # Importando corretamente a biblioteca datetime

# Credenciais AWS 
aws_access_key_id = 'ASIASFIXCUHPPBD7IL4G'
aws_secret_access_key = 'mN/uvDUe87OSGUdHVdMLtA96iX4tdPE39HVAS6P1'
aws_session_token = 'IQoJb3JpZ2luX2VjEBUaCXVzLWVhc3QtMSJGMEQCIDIUNUQkEnZ3Y1GPx+5fk2DGvd6n9fRNub7dmQPwizOKAiAyTteFSO04bI36rCYDAhUSsvuHxyL5mFBVqRFCTW/2LiqqAwiN//////////8BEAAaDDE0ODc2MTY0OTYzMCIMSU3KkkyTawnbOhb9Kv4C422tuGdk1A5LfbvCIc8iJ++IfkgmFrhxP9WOT3xnlXUjeH8Tpalbw2lWkfdqHA2XWpYG2BVQ0iGFgYJIcJOce7Jgg+zhocfFMWWEcA7dz8dFDRE2Pp4QUMlPd0vXG7jkwKH9Jbb6TS6vA4iWunJ1iylXIDfBUpv6xJDZIQ4+JkIT/mcHxN5VW5lSb6JZgKe4Xtdj6owYoThxlOHGe3EHBsY+kclGSrtAb0FOKZsGZtTzMDgHIiPinEZe7ZboPPp3vCSJ/Yv0r9JlbjgpgIslTUts1bIgI3Bd5xmZYcSon0iaAt29KkFn46cRkQy3v2lSnbj1VAlCVZ+byYZFvklWrp1kTPIANYdCEnTzZdnkUa7GC6dvIQGjQsgrBxx4yfyivg1fddR0ZwEprG5CmJWPhmKTKVGYPSfFd/qS5TbfUL92sVzqksV8jPiKt7wOtrRUYOV24J4GEPyrQnwAOs9DZoawwlejjPXXEJfLPUvKdvCRHBMpmsd+Gma/ErmlFDDv6425BjqnAUl/GdBBUC6ZGs+y4GEMUznaKSym8TV96DcL1bqDnodFxtIMMuboXglF0qDiu52kyn6z+TjmazKnRLAf6rvzxAahDOMo3ZhFFi0E/T5B35aDq+mI2ma1CIe9hxX10SqQm7rP29kaF53kcd5RqF/NFkHxjCmhp4irqMHUPcgpRXIIjKKmWMrZLqGqpbLwykOa154TzZk9tT6RuCSdsk3ri2UXubquy3n3'

# Criar um cliente S3 com as credenciais temporárias
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name='us-east-1'  
)

# Nome do bucket e arquivos
bucket = 'data-lake-de-fabiana'  # Substitua pelo nome do seu bucket

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




