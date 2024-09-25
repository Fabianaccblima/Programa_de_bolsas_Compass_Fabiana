import csv
import os  # Importar para verificar a existência de arquivos

def contar_filmes_mais_populares(arquivo):
    """Conta a frequência de cada filme em um arquivo CSV e retorna uma lista de tuplas ordenadas.

    Args:
        arquivo: O nome do arquivo CSV.

    Returns:
        Uma lista de tuplas onde as chaves são os nomes dos filmes e os valores são as contagens.
    """
    
    filmes = {}
    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Usa DictReader para facilitar o acesso por nome da coluna
        for row in reader:
            filme = row['#1 Movie']  # Acessa a coluna #1 Movie
            if filme:  # Verifica se o filme não é vazio
                if filme in filmes:
                    filmes[filme] += 1
                else:
                    filmes[filme] = 1

    filmes_ordenados = sorted(filmes.items(), key=lambda x: x[1], reverse=True)
    return filmes_ordenados

# Função para salvar resultados em um arquivo .txt
def salvar_resultados_em_txt(resultado, nome_arquivo):
    """Salva os resultados em um arquivo .txt.

    Args:
        resultado: A lista de tuplas com os resultados.
        nome_arquivo: O nome do arquivo para salvar os resultados.
    """
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as file:
            for filme, contagem in resultado:
                file.write(f"O filme '{filme}' aparece {contagem} vez(es) no dataset.\n")
        print(f"Os resultados foram salvos em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

# Exemplo de uso
arquivo_csv = 'actors.csv'  # Certifique-se de que este arquivo CSV está no mesmo diretório ou forneça o caminho completo

# Verifique se o arquivo CSV existe
if not os.path.exists(arquivo_csv):
    print(f"O arquivo '{arquivo_csv}' não foi encontrado. Verifique o caminho e tente novamente.")
else:
    resultado = contar_filmes_mais_populares(arquivo_csv)

    # Imprimindo os resultados com o nome do filme no console
    for filme, contagem in resultado:
        print(f"O filme '{filme}' aparece {contagem} vez(es) no dataset.")

    # Escrevendo os resultados em um arquivo .txt
    output_file_path = 'resultado_filmes_populares.txt'
    salvar_resultados_em_txt(resultado, output_file_path)
