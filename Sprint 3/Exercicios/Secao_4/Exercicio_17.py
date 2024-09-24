def divide_lista_em_tres(lista):

    tamanho = len(lista)
    

    tamanho_parte = tamanho // 3  
    
    # Divide a lista em três partes
    parte1 = lista[0:tamanho_parte]
    parte2 = lista[tamanho_parte:tamanho_parte * 2]
    parte3 = lista[tamanho_parte * 2:tamanho]  # Pega o restante
    
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


parte1, parte2, parte3 = divide_lista_em_tres(lista)


print(parte1,parte2,parte3)