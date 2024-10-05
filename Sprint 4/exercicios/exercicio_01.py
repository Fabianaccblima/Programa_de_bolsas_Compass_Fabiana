def processar_numeros(arquivo):
    try:
       
        with open(arquivo, 'r') as f:
            
            numeros = list(map(int, f.readlines()))

        # Filtra os números pares
        pares = list(filter(lambda x: x % 2 == 0, numeros))

        # Ordena os números pares em ordem decrescente e pega os 5 maiores
        maiores_pares = sorted(pares, reverse=True)[:5]

        # Calcula a soma dos 5 maiores pares
        soma_maiores_pares = sum(maiores_pares)
        print(maiores_pares)        
        print(soma_maiores_pares)   

    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
        
processar_numeros('number.txt')