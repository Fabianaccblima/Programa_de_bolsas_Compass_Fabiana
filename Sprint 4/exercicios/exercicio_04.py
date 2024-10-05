def calcular_valor_maximo(operadores, operandos):
    # Define uma função para aplicar a operação correspondente entre dois operandos
    operacao = lambda op, par: par[0] + par[1] if op == '+' else \
                               par[0] - par[1] if op == '-' else \
                               par[0] * par[1] if op == '*' else \
                               par[0] / par[1] if op == '/' else \
                               par[0] % par[1] if op == '%' else None
    
    # Usa zip para combinar operadores e operandos, e map para aplicar as operações
    resultados = map(lambda x: operacao(x[0], x[1]), zip(operadores, operandos))
    
    # Retorna o maior valor entre os resultados
    return max(resultados)
