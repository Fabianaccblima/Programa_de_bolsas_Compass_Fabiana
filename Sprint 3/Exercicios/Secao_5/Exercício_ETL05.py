import csv

def contar_receita_por_ator(arquivo):
    """Conta a receita total de cada ator em um arquivo CSV e retorna uma lista de tuplas ordenadas.

    Args:
        arquivo: O nome do arquivo CSV.

    Returns:
        Uma lista de tuplas onde as chaves são os nomes dos atores e os valores são as receitas totais.
    """
    
    receita_por_ator = {}
    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Usa DictReader para facilitar o acesso por nome da coluna
        for row in reader:
            ator = row['Actor'] 
            receita = row['Total Gross'] 
            
            # Converte a receita para float, substituindo possíveis vírgulas
            if receita:
                receita = float(receita.replace(',', '').replace('$', '').strip())  # Remove símbolos e espaços
                if ator in receita_por_ator:
                    receita_por_ator[ator] += receita
                else:
                    receita_por_ator[ator] = receita

    # Ordena os atores pela receita total em ordem decrescente
    atores_ordenados = sorted(receita_por_ator.items(), key=lambda x: x[1], reverse=True)
    return atores_ordenados

# Exemplo de uso
arquivo_csv = 'actors.csv'
resultado = contar_receita_por_ator(arquivo_csv)

# Imprimindo os resultados com o nome do ator e a receita total
for ator, receita in resultado:
    print(f"{ator} - ${receita:,.2f}")  # Formatação da receita para incluir vírgulas

# Escrevendo os resultados em um arquivo
output_file_path = 'actors.csv'
with open(output_file_path, 'w', encoding='utf-8') as file:
    for ator, receita in resultado:
        file.write(f"{ator} - ${receita:,.2f}\n")  # Formatação da receita para incluir vírgulas