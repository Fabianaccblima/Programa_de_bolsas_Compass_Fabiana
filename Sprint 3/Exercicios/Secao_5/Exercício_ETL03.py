import csv

# Função para encontrar o ator/atriz com a maior média de receita bruta por filme
def ator_com_maior_media(caminho_csv):
    with open(caminho_csv, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        
        maior_media = 0
        ator_com_maior_media = None
        
        for linha in leitor_csv:
            try:
                media_per_movie = float(linha['Average per Movie'])  # Converte a média por filme para float
                ator = linha['Actor']  # Obtém o nome do ator ou atriz
                
                if media_per_movie > maior_media:
                    maior_media = media_per_movie
                    ator_com_maior_media = ator
            except ValueError:
                # Ignora linhas com valores inválidos ou vazios em 'Average per Movie'
                continue
        
        if ator_com_maior_media:
            return ator_com_maior_media, maior_media
        else:
            return None, None

# Caminho do arquivo CSV
caminho_csv = 'actors.csv'

# Calcula e exibe o ator/atriz com a maior média
ator, media = ator_com_maior_media(caminho_csv)
if ator:
    print(f'O ator/atriz com a maior média de receita bruta por filme é: {ator} com {media:.2f}')
else:
    print('Não foi possível encontrar o ator/atriz com a maior média. Verifique os dados no arquivo CSV.')
