class Animar:
    def __init__(self, nome):
        self.nome = nome

class Falar(Animar):
    def falar(self):
        print(f"{self.nome} Este animal faz som.")

class Voar(Animar):
    def pode_voar(self):
        print(f"{self.nome} Este animal pode voar.")

class Nadar(Animar):
    def nadar(self):
        print(f"{self.nome} o animal está nadando!")

class Botar(Animar):
    def bota_ovo(self):
         print(f"{self.nome} Este animal consegue botar ovo.")

class Pato( Voar, Botar, Nadar, Falar):
    def __init__(self, nome):
        Animar.__init__(self, nome)   #Inicializa a classe base Animal
    
    # def nervoso(self):
    #     print(f"{self.nome}Ele está nervoso")
        
class Galinha( Voar, Botar, Falar):
    def __init__(self, nome):
        Animar.__init__(self, nome)   #Inicializa a classe base Animal
    
    def caga_molhado(self):
        print(f"{self.nome} está cagando molhado no quintal!!!!")

class Ornitorrinco( Botar, Nadar, Falar):
    def __init__(self, nome):
        Animar.__init__(self, nome)   #Inicializa a classe base Animal
    
    def peida(self):
        print(f"{self.nome} está peidando!")

class Peixe( Botar, Nadar):
    def __init__(self, nome):
        Animar.__init__(self, nome)   #Inicializa a classe base Animal




if __name__ == "__main__":
    pato = Pato("Donalt")
    pato.falar()       #Método da classe Animal
    pato.pode_voar()   #Método da classe Voar
    pato.nadar()       #Método da classe Pato
    pato.bota_ovo()    #Método da classe Bota_ovo
    galinha = Galinha("Claudete")
    galinha.falar()       #Método da classe Animal
    galinha.pode_voar()   #Método da classe Voar
    galinha.bota_ovo()    #Método da classe Bota_ovo
    ornitorrinco = Ornitorrinco("Poncio Pilátos")
    ornitorrinco.falar()       #Método da classe Animal
    ornitorrinco.nadar()       #Método da classe Pato
    ornitorrinco.bota_ovo()    #Método da classe Bota_ovo
    peixe = Peixe("Linguado")
    peixe.nadar()       #Método da classe Pato
    peixe.bota_ovo()    #Método da classe Bota_ovo