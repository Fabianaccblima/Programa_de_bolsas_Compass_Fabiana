class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

# Instanciando os objetos
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

# Usando os métodos para ordenar as listas
resultado_crescente = crescente.ordenacaoCrescente()
resultado_decrescente = decrescente.ordenacaoDecrescente()

# Imprimindo os resultados
print(resultado_crescente)  # [1, 2, 3, 4, 5]
print(resultado_decrescente)  # [9, 8, 7, 6]

