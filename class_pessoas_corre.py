class Pessoa:
    def __init__(self, nome = "", sexo = "", cpf ="", ano_nascimento = 0, salário_bruto = 0.0):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nascimento = ano_nascimento
        self.salário_bruto = salário_bruto
        self.idade = self.calcular_idade()
        self.líquido = self.salário_líquido()
    
    def calcular_idade(self):
        return 2024 - self.ano_nascimento
    
    def salário_líquido(self):
        if self.salário_bruto == 1412.00 :
            print("- INSS")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 7.5) /100)
            return self.salário_bruto - 92.5 / 100
        elif self.salário_bruto >= 1412.01 and self.salário_bruto <=2666.68:
            print("- INSS")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 9.0) /100)
            return self.salário_bruto - 91.0 /100
        elif self.salário_bruto >= 2259.21 and self.salário_bruto <= 2826.65 :
            print("- IRRF")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 7.5) /100)
            return self.salário_bruto - 92.5 / 100
        elif self.salário_bruto >= 2826.66 and self.salário_bruto <= 3751.05 :
            print("- IRRF")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 15.0) /100)
            return self.salário_bruto - 85 / 100
        elif self.salário_bruto >= 3751.06 and self.salário_bruto <= 4664.68:
            print("- IRRF")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 22.5) /100)
            return self.salário_bruto - 77.5 / 100
        
        elif self.salário_bruto >= 4664.69:
            print("- IRRF")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 27.5) /100)
            return self.salário_bruto - 72.5 / 100
        elif self.salário_bruto >= 2666.69 and self.salário_bruto <=4000.03:
            print("- INSS")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 12.0) /100)
            return self.salário_bruto - 88.0 / 100
        elif self.salário_bruto >= 4000.04 :
            print("- INSS")
            self.líquido = self.salário_bruto - ((self.salário_bruto * 14.0) /100)
            return self.salário_bruto - 86.0 / 100


if __name__=='__main__':
    # primeiro_cidadão = Pessoa("Bruce Banner", "Masculino", "123.456.789-00", 2002)
    # print(primeiro_cidadão.idade)
    pessoa_input = Pessoa()
    pessoa_input.nome = input("Digite seu nome:")
    pessoa_input.sexo = input("Digite seu sexo:")
    pessoa_input.cpf = input("Digite o seu cpf:")
    pessoa_input.ano_nascimento = input("Digite o ano que nasceu:")
    pessoa_input.salário_bruto = float(input("Digite seu salário: R$ "))
    pessoa_input.salário_líquido()
    print(pessoa_input.nome)
    print(pessoa_input.sexo)
    print(pessoa_input.cpf)
    print(pessoa_input.ano_nascimento)
    print("R$",pessoa_input.líquido)