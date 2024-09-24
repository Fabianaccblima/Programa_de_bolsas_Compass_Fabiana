import csv

# Função para calcular a média da coluna 'Gross'
def calcular_media_gross(caminho_csv):
    with open(caminho_csv, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        
        soma_gross = 0
        total_filmes = 0
        
        for linha in leitor_csv:
            try:
                gross = float(linha['Gross'])  # Converte a receita bruta para float
                soma_gross += gross
                total_filmes += 1
            except ValueError:
                # Ignora linhas com valores inválidos ou vazios em 'Gross'
                continue
        
        # Calcula a média se houver algum filme válido
        if total_filmes > 0:
            media_gross = soma_gross / total_filmes
            return media_gross
        else:
            return None

# Caminho do arquivo CSV
caminho_csv = 'actors.csv'

# Calcula e exibe a média
media = calcular_media_gross(caminho_csv)
if media is not None:
    print(f'A média da receita bruta (Gross) é: {media:.2f}')
else:
    print('Não foi possível calcular a média. Verifique os dados no arquivo CSV.')


