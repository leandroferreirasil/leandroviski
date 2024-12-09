class cachorro:
    def __init__(self, raça, cor, nome, sexo, peso, altura, data_nascimento, quantidade_comida_porção):
        self.raça = raça
        self.cor = cor
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.quantidade_comida_porção = quantidade_comida_porção
        self.comida = 1000

    def imprima_inf(self):
        print(f"O Cachorro {self.nome} possui os atributos: \n Cor -{self.cor} ;\n Raça - {self.raça} ;\n Sexo - {self.sexo} ;\n Peso - {self.peso} ;\n Tem - {self.altura} cm de Altura; \n Nasceu - {self.data_nascimento} ;\n Come - {self.quantidade_comida_porção} gramas por dia;")

    def comer(self):
        self.comida -= self.quantidade_comida_porção
        print(f" O Cachorro {self.nome} ainda possui {self.comida} gramas.")  

    def latir(self):
        print(f" O cachorro {self.nome} está latindo!!!")
if __name__ == '__main__':
    meu_primeiro_cachorro = cachorro("Cofap", "Amarron", "Vina", "FÊMEA", 5.590, 32.5, "01/01/2024",80 )
    print(meu_primeiro_cachorro.nome)
    segundo_cachorro      = cachorro("SRD ", "Caramelo", "Thor", "MACHO", 15.670, 40.9,"09/05/2024",150)
    print(segundo_cachorro.nome)
    print(type(segundo_cachorro))
    meu_primeiro_cachorro.imprima_inf()
    meu_primeiro_cachorro.comer()
    meu_primeiro_cachorro.latir()
    segundo_cachorro.imprima_inf()
    segundo_cachorro.comer()
    segundo_cachorro.latir()
    #terceiro_cachorro = cachorro(" Poodie - Mestiça ", "Branca", "Lady", "fem",10.80,38.7,)