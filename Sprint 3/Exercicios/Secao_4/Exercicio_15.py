class Lampada:
    def __init__(self, ligada):
        # O atributo ligada é um booleano: True se ligada, False se desligada
        self.ligada = ligada
    
    def liga(self):
        # Muda o estado para True (ligada)
        self.ligada = True
    
    def desliga(self):
        # Muda o estado para False (desligada)
        self.ligada = False
    
    def esta_ligada(self):
        # Retorna True se a lâmpada estiver ligada, False caso contrário
        return self.ligada

# Testando a classe Lampada
lampada = Lampada(False)  # Inicia a lâmpada como desligada

# Liga a lâmpada
lampada.liga()

# Imprime se a lâmpada está ligada
print(f"A lâmpada está ligada? {lampada.esta_ligada()}")  # Deve imprimir: True

# Desliga a lâmpada
lampada.desliga()

# Imprime se a lâmpada ainda está ligada
print(f"A lâmpada ainda está ligada? {lampada.esta_ligada()}")  # Deve imprimir: False
