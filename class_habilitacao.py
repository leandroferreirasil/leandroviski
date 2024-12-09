class cnh:
    def __init__(self, nivel = 0, emissao="", validade = "" , digite= 0, cat_hab = ""):
        self._nivel      =   nivel
        self._emissao    =   emissao
        self._validade   =   validade
        self._cat_hab    =   cat_hab
        self._digite     =   digite

    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_emissao(self):
        return self._emissao
    
    def set_emissao(self, emissao):
        self._emissao = emissao

    def get_validade(self):
        return self._validade
    
    def set_validade(self, validade):
        self._validade = validade

    def get_cat_hab(self):
        return self._cat_hab
    
    def set_cat_hab(self, cat_hab):
        self._cat_hab = cat_hab

    def cadastrar(self):
        print("  SEJA BEM VINDO!!!!!\n Cadastre os Dados da sua Habilitação>>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n")
        self._nivel  = int(input("Digite seu nível:"))
        self._emissao  = input("Digite sua data de emissao:")
        self._validade  = input("Digite a data de validade:")
        self._cat_hab  = input("Digite a categoria da cnh:")

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
        self._emissao    =   ""
        self._validade   =   ""
        self._cat_hab    =   ""
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
        print(f" SUA CNH!!!\n Data de Emissão: {self._emissao} \n Até quando é Valida: {self._validade}\n Categoria: {self._cat_hab}")
        print("---------------------------------------------------")
        
        

if __name__ == '__main__':
    cnh_input = cnh()
    cnh_input.cadastrar()
    cnh_input.funcao()
    cnh_input.verificar_nivel()