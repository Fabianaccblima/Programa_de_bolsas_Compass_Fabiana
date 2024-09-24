class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None  # Atributo privado

    @property
    def nome(self):
        return self.__nome  # Método para retornar o valor de __nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome  # Método para definir o valor de __nome

# Exemplo de uso
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'  # Define o nome
print(pessoa.nome)  # Retorna o nome
