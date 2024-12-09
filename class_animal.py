class Animal :
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print(f"{self.nome} faz um som.")
class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} late.")
class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} mia.")

if __name__ == "__main__":
    cachorro = Cachorro("Rex")
    gato = Gato("Mimi")
    cachorro.fazer_som()
    gato.fazer_som()
    cachorro_2 = Cachorro("Pluto")
    gato_2 = Gato("Bob")
    cachorro_2.fazer_som()
    gato_2.fazer_som()