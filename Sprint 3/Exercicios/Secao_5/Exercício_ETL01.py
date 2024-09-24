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
                num_filmes = float(linha[1])  # Tenta converter para float primeiro
                if num_filmes > max_filmes:
                    max_filmes = num_filmes
                    ator_com_mais_filmes = nome_ator
            except ValueError:
                print(f"Linha inválida: {linha}. Ignorando...")

    return ator_com_mais_filmes, max_filmes


arquivo_csv = caminho = "actors.csv"

ator, filmes = processar_arquivo(arquivo_csv)

print(f"O ator/atriz com mais filmes é {ator} com {filmes} filmes.")