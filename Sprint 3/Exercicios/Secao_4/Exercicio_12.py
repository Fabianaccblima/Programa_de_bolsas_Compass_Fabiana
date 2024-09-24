##Funçao para elevar um numero a 2
def potencia(lista):
 
  lista_potencia = [numero ** 2 for numero in lista]
  return lista_potencia
 
 
#função eleva a 2 as ocorrencias da lista
def my_map(lista_in, funcao_in):
 
    lista_out = funcao_in(lista_in)
    return lista_out
 
# Inicio programa
 
lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
lista_final = my_map(lista_num, potencia)
 
print(lista_final)