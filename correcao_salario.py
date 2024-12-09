class Pessoa:
    def __init__(self, nome = "", sexo = "", cpf ="", ano_nascimento = 0, salário_bruto = 0.0):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nascimento = ano_nascimento
        self.idade = self.calcular_idade()
        self.salário_bruto = salário_bruto
        self.salário_líquido = self.calcular_salário_líquido()
    def calcular_desconto_inss(self):
        salário = self.salário_bruto
        if salário <= 1412.00:
            return self.calcular_porcentagem(7.5)
        elif salário < 1412.00 and salário <= 2666.68:
             return self.calcular_porcentagem(9.0)
        elif salário > 2666.68 and salário <= 4000.03:
             return self.calcular_porcentagem(12.00) 
        else:
             return self.calcular_porcentagem(14.00)
        
    def calcular_desconto_irrf(self):
        salário = self.salário_bruto
        if salário >= 2259.21 and salário <= 2826.65:
            return self.calcular_porcentagem(7.5)
        elif salário > 2826.66 and salário <= 3751.05:
            return self.calcular_porcentagem(15.00)
        elif salário > 3751.05 and salário <= 4664.68:
            return self.calcular_porcentagem(22.5)
        elif salário > 4664.08:
            return self.calcular_porcentagem(27.5)   
        else:
            return 0.0
        
    def calcular_porcentagem(self, porcentagem):
         return (self.salário_bruto * porcentagem) /100 
    
    def imprimir_dados(self): 
        print(f"Nome: {self.nome} \nAno nascimento: {self.ano_nascimento} \nCpf:{self.cpf} \nSexo:{self.sexo} \nBruto:{self.salário_bruto} \nLíquido:{self.salário_líquido} \nIdade:{self.idade}")
    
    def calcular_salário_líquido(self):
        return self.salário_bruto - (self.calcular_desconto_inss() + self.calcular_desconto_irrf())
    
    def calcular_idade(self):
        return 2024 - self.ano_nascimento
    
if __name__=='__main__':
    pessoa_1 = Pessoa("Bruce Banner", "Masculino", "123.456.789-00", 2002,1412.00)
    # print(roud(pessoa_1.salário_líquido,2))
    pessoa_1.imprimir_dados()
    pessoa_2.input = Pessoa()
    pessoa_2.input.nome = input("Digite seu nome:")
    pessoa_2.input.cpf = input("Digite o seu cpf:")
    pessoa_2.input.salário_bruto = float(input("Digite seu salário: R$ "))
    pessoa_2.input.ano_nascimento = int(input("Digite o ano que nasceu:"))
    pessoa_2.input.sexo = input("Digite seu sexo:")
    pessoa_2.
    pessoa_2_input.calcular_idade()
    pessoa_2_input.salário_bruto = float(input("Digite seu salário: R$ "))
    pessoa_2_input.calcular_desconto_inss()
    pessoa_2_input.calcular_desconto_irrf()
    pessoa_2_input.salário_líquido()
    print(pessoa_2_input.nome)
    print(pessoa_2_input.sexo)
    print(pessoa_2_input.cpf)
    print(pessoa_2_input.idade)
    print("R$",pessoa_2_input.salário_líquido)