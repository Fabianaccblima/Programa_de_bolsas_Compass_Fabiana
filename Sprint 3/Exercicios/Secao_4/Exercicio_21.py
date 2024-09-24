class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

# Criando instâncias das classes
pato = Pato()
pardal = Pardal()

# Imprimindo as informações do Pato
print("Pato")
pato.voar()
pato.emitir_som()

# Imprimindo as informações do Pardal
print("Pardal")
pardal.voar()
pardal.emitir_som()
