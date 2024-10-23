import boto3
import pandas as pd
 
# Configuração do cliente S3 com credenciais temporárias
s3 = boto3.client(
    's3',
    aws_access_key_id='ASIASFIXCUHPIQ6U77TN',
    aws_secret_access_key='XytW6DVPekU7Iw05OyPfBDgnsxOlCLUvt+vpeJDW',
    region_name='us-east-1',
    aws_session_token='IQoJb3JpZ2luX2VjEEAaCXVzLWVhc3QtMSJIMEYCIQCueZAcMVUL3ZuPg7ke2sSHSJBapX8/zNlnEZEjds52XAIhAIbRh/dpv62EDxSfBOlSAKuu4khv5jUcYmngl2SmFroJKqoDCKn//////////wEQABoMMTQ4NzYxNjQ5NjMwIgyqGP+Z622ns6HDsWAq/gJjicnHMHbzWhfKjGHpPNoCwYEL64ft1zsZ8Knptzv8RclDiZLCjCofwCidLAJclBowwcUL7fFo6IqC9MbGvVGA042efDVC2Q59oKpS0YB+fx9maWk630KkmssQpPm6Yz+/f5LY5gydF3CcI3Hxmb3tqUQl+4zQX9qgTwz/DxJ3Bt1SmM07sXyVkASyFR9XTsmHCXzgVsQoYR1QBzWNKdz92YDXg1R/FcjHuvhVTZwUSTAOodztQrTMmXHcrdqVNcsEGJ9aJBgM2XVVxaIu4e+rguB/YfOZ5TtJgnghXO/HJM7mBl5kYuUrIziJfzfFoaMfqY+1JA9w/TaPdw8+sKpivBT/rDTOmkOrhIRc5g7QmYHrVV2OOot2PKgYVPMa7nFPZEq2IEnoWIWcYS+HsNvgfcuuUGL+NXi5yh30qSyA+RNOhB7Df3iaxbWHbFKIkr8J/AjOqPdV2enWy3F2PAtQ3vczEhGrHDqi6iRj/es3x7scsoZiGJT0FbIeaYswMMWZ37gGOqUBRIKh+FR1aDbylbfBZ0MI1KrGaS4pO7sm5lxuJuRxyeUrMJe6HJhVLFt8fMWW6tpYLozgbLy1du/Xp4NznWtu5mZ9GkfUtdUllKonmhIRe8MGZH6pI3uhjdvFa67l40Y2Ana3ZF64lK/saEst98puGuLRULI2DLHyqxW6M0a3zHtNqy9w72tpe6WHrI3549hOeNtfXlNUHLucbjWgZpM5KRkzpKhA'
)
 
# Download do arquivo do S3
bucket_name = 'desafioaws'
file_name = 'chegadas_tb_2023.csv'
s3.download_file(bucket_name, file_name, file_name)
 
# Leitura do arquivo CSV a partir do caminho especificado, utilizando ';' como delimitador e 'latin1' para decodificação de caracteres.
df = pd.read_csv(file_name, delimiter=';', encoding='latin1')
 
# Filtragem, conversões e agregações em um único comando
result = (
    df.assign(
        data=pd.to_datetime(df['data'], errors='coerce'),  # Conversão de data
        País=df['País'].str.upper()                           # Conversão para maiúsculas
    )
    .query("Continente == 'Europa' and País != 'TURQUIA' and data.dt.month == 7")  # Filtragem com operadores lógicos
    .groupby('País')  # Agrupamento por País
    .agg(
        total_chegadas=('Chegadas', 'sum'),  # Função de agregação para soma
        media_chegadas=('Chegadas', 'mean')   # Função de agregação para média
    )
    .reset_index()  # Resetando o índice
    .query("total_chegadas > 50")  # Condição similar ao HAVING
)
 

# Salvar o resultado em um novo arquivo CSV
output_file = 'resultado_chegadas.csv'
result.to_csv(output_file, index=False, sep=';', encoding='utf-8')

# Fazer o upload do novo arquivo CSV para o bucket S3
output_key = 'resultado_chegadas.csv'
s3.upload_file(output_file, bucket_name, output_key)

print(f'O arquivo {output_file} foi gerado e enviado para o bucket {bucket_name} com sucesso.')