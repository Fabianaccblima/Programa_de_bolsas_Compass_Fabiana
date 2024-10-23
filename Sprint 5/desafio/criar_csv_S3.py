import boto3

# Credenciais AWS 
aws_access_key_id = 'ASIASFIXCUHPIQ6U77TN'
aws_secret_access_key = 'XytW6DVPekU7Iw05OyPfBDgnsxOlCLUvt+vpeJDW'
aws_session_token = 'IQoJb3JpZ2luX2VjEEAaCXVzLWVhc3QtMSJIMEYCIQCueZAcMVUL3ZuPg7ke2sSHSJBapX8/zNlnEZEjds52XAIhAIbRh/dpv62EDxSfBOlSAKuu4khv5jUcYmngl2SmFroJKqoDCKn//////////wEQABoMMTQ4NzYxNjQ5NjMwIgyqGP+Z622ns6HDsWAq/gJjicnHMHbzWhfKjGHpPNoCwYEL64ft1zsZ8Knptzv8RclDiZLCjCofwCidLAJclBowwcUL7fFo6IqC9MbGvVGA042efDVC2Q59oKpS0YB+fx9maWk630KkmssQpPm6Yz+/f5LY5gydF3CcI3Hxmb3tqUQl+4zQX9qgTwz/DxJ3Bt1SmM07sXyVkASyFR9XTsmHCXzgVsQoYR1QBzWNKdz92YDXg1R/FcjHuvhVTZwUSTAOodztQrTMmXHcrdqVNcsEGJ9aJBgM2XVVxaIu4e+rguB/YfOZ5TtJgnghXO/HJM7mBl5kYuUrIziJfzfFoaMfqY+1JA9w/TaPdw8+sKpivBT/rDTOmkOrhIRc5g7QmYHrVV2OOot2PKgYVPMa7nFPZEq2IEnoWIWcYS+HsNvgfcuuUGL+NXi5yh30qSyA+RNOhB7Df3iaxbWHbFKIkr8J/AjOqPdV2enWy3F2PAtQ3vczEhGrHDqi6iRj/es3x7scsoZiGJT0FbIeaYswMMWZ37gGOqUBRIKh+FR1aDbylbfBZ0MI1KrGaS4pO7sm5lxuJuRxyeUrMJe6HJhVLFt8fMWW6tpYLozgbLy1du/Xp4NznWtu5mZ9GkfUtdUllKonmhIRe8MGZH6pI3uhjdvFa67l40Y2Ana3ZF64lK/saEst98puGuLRULI2DLHyqxW6M0a3zHtNqy9w72tpe6WHrI3549hOeNtfXlNUHLucbjWgZpM5KRkzpKhA'

# Criar um cliente S3 com as credenciais temporárias
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name='us-east-1'  
)

# Nome do bucket e arquivo
bucket = 'desafioaws'
arquivo = r'C:\Users\fabia\OneDrive\Área de Trabalho\Teste_Sprint05\chegadas_tb_2023.csv'
nome_arquivo = 'chegadas_tb_2023.csv'

try:
    # Criar o bucket (ignorar se o bucket já existir)
    s3.create_bucket(Bucket=bucket)
    print(f'Bucket "{bucket}" criado com sucesso ou já existente.')

    # Fazer upload do arquivo para o bucket
    s3.upload_file(arquivo, bucket, nome_arquivo)
    print(f'Arquivo "{nome_arquivo}" enviado para o bucket "{bucket}" com sucesso!')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
