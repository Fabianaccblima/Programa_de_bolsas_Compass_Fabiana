class Calculo:
    def soma(self, x, y):
        return x + y

    def subtrai(self, x, y):
        return x - y

# Testando a classe Calculo
x = 4
y = 5

calculadora = Calculo()

# Realizando os cálculos e imprimindo os resultados
resultado_soma = calculadora.soma(x, y)
resultado_subtracao = calculadora.subtrai(x, y)

print(f"Somando: {x}+{y} = {resultado_soma}")
print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")
