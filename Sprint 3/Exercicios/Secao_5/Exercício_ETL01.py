import csv

def processar_arquivo(arquivo):
    
  
    with open(arquivo, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Assumindo que a primeira linha é o cabeçalho
        next(reader)

        max_filmes = 0
        ator_com_mais_filmes = ""

        for linha in reader:
            try:
                nome_ator = linha[0]
                num_filmes = float(linha[1])  # converter para float primeiro
                if num_filmes > max_filmes:
                    max_filmes = num_filmes
                    ator_com_mais_filmes = nome_ator
            except ValueError:
                print(f"Linha inválida: {linha}. Ignorando...")

    return ator_com_mais_filmes, max_filmes

def salvar_resultado_em_txt(ator, filmes, nome_arquivo):
    """Salva o resultado em um arquivo .txt.

    Args:
        ator: O nome do ator.
        filmes: O número de filmes.
        nome_arquivo: O nome do arquivo para salvar o resultado.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(f"O ator/atriz com mais filmes é {ator} com {filmes} filmes.\n")

# Caminho do arquivo CSV
arquivo_csv = "actors.csv"

# Processar o arquivo para encontrar o ator com mais filmes
ator, filmes = processar_arquivo(arquivo_csv)

# Exibir o resultado no console
print(f"O ator/atriz com mais filmes é {ator} com {filmes} filmes.")

# Salvar o resultado em um arquivo .txt
output_file_path = 'resultado_atores.txt'
salvar_resultado_em_txt(ator, filmes, output_file_path)

print(f"O resultado também foi salvo em '{output_file_path}'.")
