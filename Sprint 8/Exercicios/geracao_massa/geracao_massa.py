# Importação das bibliotecas necessárias
import os
import random
import datetime
import names  


# Inicializar uma lista com 250 números inteiros aleatórios
numeros_aleatorios = [random.randint(1, 100) for _ in range(250)]

# Reverter a ordem dos elementos da lista
numeros_aleatorios.reverse()

# Exibir a lista após a reversão
print("Lista de números inteiros após a inversão:")
print(numeros_aleatorios)

#  Criar uma lista contendo 20 espécies de animais
lista_animais = ['Cachorro', 'Gato', 'Elefante', 'Tigre', 'Leão', 'Pássaro', 'Cavalo', 
                 'Coelho', 'Peixe', 'Macaco', 'Golfinho', 'Girafa', 'Camelo', 'Serpente', 
                 'Papagaio', 'Rato', 'Porco', 'Vaca', 'Ovelha', 'Pato']

# Ordenar a lista de animais em ordem alfabética
lista_animais.sort()

# Exibir a lista de animais ordenada
print("\nLista de animais em ordem alfabética:")
for animal in lista_animais:
    print(animal)

# Salvar a lista de animais em um arquivo CSV (um animal por linha)
with open('animais_ordem.csv', 'w', encoding='utf-8') as arquivo:
    for animal in lista_animais:
        arquivo.write(f"{animal}\n")

print("\nLista de animais salva em 'animais_ordem.csv'")


# Definir a semente aleatória para garantir resultados reprodutíveis
random.seed(42)

# Número de nomes únicos a serem gerados e a quantidade total de nomes
quantidade_nomes_unicos = 3000
quantidade_nomes_total = 10000000

# Criar uma lista de nomes únicos
nomes_unicos = [names.get_full_name() for _ in range(quantidade_nomes_unicos)]

# Informar que a geração dos nomes está em processo
print("\nGerando {} nomes aleatórios...".format(quantidade_nomes_total))

# Criar a lista de nomes aleatórios selecionados da lista de nomes únicos
nomes_aleatorios = [random.choice(nomes_unicos) for _ in range(quantidade_nomes_total)]

# Salvar os nomes gerados em um arquivo de texto
with open("nomes_aleatorios.txt", "w", encoding="utf-8") as arquivo_txt:
    arquivo_txt.write("\n".join(nomes_aleatorios))

print("\nArquivo 'nomes_aleatorios.txt' executado com sucesso!")
