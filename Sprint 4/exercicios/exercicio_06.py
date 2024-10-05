def maiores_que_media(conteudo):
    # Calcula a média dos preços
    media = sum(conteudo.values()) / len(conteudo)

    # Filtra produtos cujo valor é superior à média
    produtos_acima_da_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]

    # Retorna os produtos ordenados pelo preço em ordem crescente
    return sorted(produtos_acima_da_media, key=lambda item: item[1])
