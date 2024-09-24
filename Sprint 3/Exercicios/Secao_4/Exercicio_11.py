import json


# Caminho para o arquivo JSON
caminho_arquivo = 'person.json'

# Abrir e ler o arquivo JSON
with open(caminho_arquivo, 'r') as arquivo:
    
    conteudo = json.load(arquivo)

# Imprimir o conteúdo
print(conteudo)