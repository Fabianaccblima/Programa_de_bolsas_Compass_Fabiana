def imprimir_parametros_simples(*args, **kwargs):
    # Imprime os parâmetros não nomeados (args)
    for arg in args:
        print(arg)
    
    # Imprime os valores dos parâmetros nomeados (kwargs)
    for value in kwargs.values():
        print(value)

# Testando a função com os parâmetros fornecidos
imprimir_parametros_simples(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
