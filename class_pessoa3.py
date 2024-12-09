class pessoa:
    def __init__(self, nome, sexo, Cpf, data_nascimento, ano_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.ano_nascimento = ano_nascimento
        self.sexo = sexo
        self.Cpf = Cpf
        
    def imprima_inf(self):
        print("---------------------------------------------------")
        print(f" {self.nome} tem suas características: \n Nome - {self.nome}\n Sexo - {self.sexo}\n Cpf - {self.Cpf}\n Data de Nascimento - {self.data_nascimento}\n Ano que Nasceu {self.ano_nascimento}")
        
    def calcular_idade(self):
        self.ano_nascimento -= 2024
        print(f"{self.nome} tem {self.ano_nascimento} de idade")  

if __name__ == '__main__':
    primeira_pessoa = pessoa("Robson", "Masculino", "116.890.897-06", "09/09/2009", "2009")
    print(primeira_pessoa.nome)
    print(type(primeira_pessoa))
    segunda_pessoa = pessoa("Felícica", "Femenino", "345.567.123-08", "02/12/2001", "2001")
    print(segunda_pessoa.nome)
    print(type(segunda_pessoa))
    primeira_pessoa.imprima_inf()
    primeira_pessoa.calcular_idade()
    segunda_pessoa.imprima_inf()
    segunda_pessoa.calcular_idade()