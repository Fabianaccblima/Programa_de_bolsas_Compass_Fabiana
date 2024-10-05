import csv

def processar_notas(arquivo):
    """Processa um arquivo CSV com notas de estudantes e gera um relatório.

    Args:
        arquivo (str): Nome do arquivo CSV.
    """

    with open(arquivo, 'r') as csvfile:
        reader = csv.reader(csvfile)
        resultados = []

        for linha in reader:
            # Verifica se a linha contém dados válidos (evita linhas vazias ou com dados faltantes)
            if len(linha) >= 2:
                nome = linha[0]
                notas = list(map(int, linha[1:]))  # Converte as notas para inteiros
                tres_maiores = sorted(notas, reverse=True)[:3]
                media = round(sum(tres_maiores) / 3, 2)  # Média com duas casas decimais
                resultados.append(f"Nome: {nome} Notas: {tres_maiores} Média: {media}")

        # Ordena os resultados pelo nome do estudante
        for resultado in sorted(resultados):
            print(resultado)

# Exemplo de uso:
processar_notas('estudantes.csv')