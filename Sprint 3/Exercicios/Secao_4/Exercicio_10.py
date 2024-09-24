def remover_duplicatas(lista):
    # Converte a lista em um conjunto (set) para remover duplicatas, depois volta para lista
    return list(set(lista))

# Testando a função com a lista fornecida
lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remover_duplicatas(lista_teste)

# Imprimindo a nova lista sem duplicatas
print(resultado)
