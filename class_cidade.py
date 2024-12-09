class cidade:
    def __init__(self, nivel = 0, cidade="", estado = "" , digite= 0, cep = ""):
        self._nivel      =   nivel
        self._cidade     =   cidade
        self._estado     =   estado
        self._cep        =   cep
        self._digite     =   digite

    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_cidade(self):
        return self._cidade
    
    def set_cidade(self, cidade):
        self._cidade = cidade

    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        self._estado = estado

    def get_cep(self):
        return self._cep
    
    def set_cep(self, cep):
        self._cep = cep

    def cadastrar(self):
        print("  SEJA BEM VINDO!!!!!\n Cadastre Dados da sua Cidade>>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n")
        self._nivel          = int(input("Digite seu nivel:"))
        self._cidade         = input("Digite sua Cidade:")
        self._estado         = input("Digite Estado:")
        self._cep            = input("Digite seu CEP:")

    def verificar_nivel(self):
            print("---------------------------------------------------")
            if self._nivel == 1:
                print("Nível 1 - Cliente")
            elif self._nivel == 2:
                print("Nível 2 - Fornecedor")
            elif self._nivel == 3:
                print("Nível 3 - Funcionário")
            elif self._nivel == 4:
                print("Nível 4 - Gerente")
            elif self._nivel == 5:
                print("Nível 5 - Motorista")
            elif self._nivel == 6:
                print("Nível 6 - Entregador")
            else:
                print("Nível inválido")
            

            self.imprima_inf()
            
       
    def limpa(self):
        # Redefinindo os atributos para valores padrão
        self._nivel      =   0
        self._cidade     =   ""
        self._estado     =   ""
        self._cep        =   ""
        self.imprima_inf()

    def funcao(self):
        print("---------------------------------------------------")
        print(" DIGITE:\n1- ATUALIZAR DADOS\n2- DELETAR DADOS\n3- IMPRIMIR DADOS")
        self._digite = int(input(":"))
        
        if self._digite == 1:
            self.cadastrar()

        elif self._nivel == 2:
            self.limpa()
    
        else:
            self.verificar_nivel()


    def imprima_inf(self):
        
        print(f" TUDO SOBRE SUA CIDADE!!!\n Cidade:{self._cidade} \n Estado:{self._estado} Cep: {self._cep}")
        print("---------------------------------------------------")
        
        

if __name__ == '__main__':
    cidade_input = cidade() 
    cidade_input.cadastrar()
    cidade_input.imprima_inf()
    