a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Criando uma nova lista vazia
impares = []

# Iterando sobre a lista original e adicionando os números ímpares à nova lista
for i in a:
    if i % 2 != 0:
        impares.append(i)

# Imprimindo a nova lista
print(impares)