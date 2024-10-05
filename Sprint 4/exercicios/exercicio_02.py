def conta_vogais(texto):
    # Define as vogais
    vogais = 'aeiouAEIOU'
    
    # Filtra apenas os caracteres que são vogais
    apenas_vogais = filter(lambda char: char in vogais, texto)
    
    # Retorna a contagem das vogais usando len
    return len(list(apenas_vogais))
