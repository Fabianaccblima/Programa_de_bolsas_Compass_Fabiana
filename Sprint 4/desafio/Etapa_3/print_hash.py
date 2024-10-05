import hashlib
 
def print_hash(mensagem):    
    # Cria um objeto hash SHA-1
    hash_sha1 = hashlib.sha1()
 
    # Atualiza o objeto com os dados 
    hash_sha1.update(mensagem.encode('utf-8'))
 
    # Gera o hash e o retorna em formato hexadecimal
    hash_hex = hash_sha1.hexdigest()
 
    print(f"Hash SHA-1 em hexadecimal: {hash_hex}")
 
while True:
    # Solicita a entrada do usuário
    mensagem = input("Digite uma mensagem (ou pressione Enter para sair): ")
 
    # Se o usuário pressionar Enter sem digitar nada, o loop é encerrado
    if mensagem == "":
        print("Encerrando o programa.")
        break
 
    # Chama a função para calcular o hash da mensagem
    print_hash(mensagem)