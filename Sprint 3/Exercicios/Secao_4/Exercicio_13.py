# Caminho para o arquivo de texto
caminho_arquivo = 'arquivo_texto.txt'

# Abrir e ler o arquivo de texto
with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

# Imprimir o conteúdo, garantindo que uma nova linha seja adicionada no final
print(conteudo, end='')
