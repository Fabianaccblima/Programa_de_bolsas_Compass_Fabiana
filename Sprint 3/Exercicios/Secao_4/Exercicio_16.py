def soma_numeros(string_numeros):
    # Divide a string em uma lista de números (como strings) separados por vírgula
    numeros = string_numeros.split(',')
    
    # Converte cada elemento da lista para um inteiro e calcula a soma
    soma = sum(int(numero) for numero in numeros)
   
    # Retorna a soma dos números 
    return soma
 
# Testando a função com a string fornecida
string_numeros = "1,3,4,6,10,76"
valor_final = soma_numeros(string_numeros)

# Imprime a mensagem com o formato correto
print(valor_final)