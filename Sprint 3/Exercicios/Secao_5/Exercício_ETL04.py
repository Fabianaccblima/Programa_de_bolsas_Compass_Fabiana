import csv

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

# Exemplo de uso
arquivo_csv = 'actors.csv'
resultado = contar_filmes_mais_populares(arquivo_csv)

# Imprimindo os resultados com o nome do filme
for filme, contagem in resultado:
    print(f"O filme '{filme}' aparece {contagem} vez(es) no dataset.")

# Escrevendo os resultados em um arquivo
output_file_path = 'actors.csv'
with open(output_file_path, 'w', encoding='utf-8') as file:
    for filme, contagem in resultado:
        file.write(f"O filme '{filme}' aparece {contagem} vez(es) no dataset.\n")