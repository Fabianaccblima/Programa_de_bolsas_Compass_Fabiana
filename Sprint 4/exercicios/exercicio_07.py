def pares_ate(n: int):
    # Utiliza um laço for para gerar números pares de 2 até n
    for i in range(2, n + 1, 2):
        yield i  # O 'yield' transforma a função em um generator
