import random

random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

# Calcula o valor mínimo e máximo
valor_minimo = min(random_list)
valor_maximo = max(random_list)

# Calcula a média
media = sum(random_list) / len(random_list)

# Ordena a lista para calcular a mediana
random_list.sort()

# Calcula a mediana
if len(random_list) % 2 == 0:
    mediana = (random_list[len(random_list) // 2 - 1] + random_list[len(random_list) // 2]) / 2
else:
    mediana = random_list[len(random_list) // 2]

# Exibe os resultados em uma única linha
print(f"Media: {media:.2f}, Mediana: {mediana:.1f}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")