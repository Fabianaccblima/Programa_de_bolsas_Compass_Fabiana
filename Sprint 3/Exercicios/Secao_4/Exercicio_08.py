# Lista de palavras
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

# Função para verificar se uma palavra é um palíndromo
def verificar_palindromo(palavra):
    if palavra == palavra[::-1]:  # Verifica se a palavra é igual à sua inversa
        return True
    return False

# Verificando cada palavra na lista e imprimindo o resultado
for palavra in palavras:
    if verificar_palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")
