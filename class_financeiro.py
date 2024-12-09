class financeiro:
    def __init__(self, nivel =  0, forma ="", c_d ="", digite = 0, pix_cartao ="", valor= ""):
        self._nivel          =   nivel
        self._forma          =   forma
        self._c_d            =   c_d
        self._pix_cartao     =   pix_cartao
        self._valor          =   valor
        self._digite         =   digite

    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_forma(self):
        return self._forma
    
    def set_forma(self, forma):
        self._forma = forma

    def get_c_d(self):
        return self._c_d
    
    def set_c_d(self, c_d):
        self._c_d = c_d

    def get_pix_cartao(self):
        return self._pix_cartao
    
    def set_pix_cartao(self, pix_cartao):
        self._pix_cartao = pix_cartao

    def get_valor(self):
        return self._valor
    
    def set_valor(self, valor):
        self._valor = valor
        
    def cadastrar(self):
        print("  SEJA BEM VINDO!!!!!\n Cadastre seus Dados financas >>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n")
        self._nivel          = int(input("Digite seu nivel:"))
        self._forma          = input("Digite sua forma de pagamento:")
        self._c_d            = input("Será no Crédito ou Débito?:")
        self._pix_cartao     = input("Digite seu Pix OU Número do cartão\n(Se essa for sua forma de Pagemento):")
        self._valor          = input("Crie uma senha\n(Obrigatório conter letras números e simbolos):")

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
        self._nivel          =   0
        self._forma          =   ""
        self._c_d            =   ""
        self._pix_cartao     =   ""
        self._valor          =   ""
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
        
        print(f" SEUS DADOS FINACIEROS =======\n Forma de Pagamento:{self._forma}\n Será no {self._c_d}\n Número do Cartão ou Pix: {self._pix_cartao}\n Valor total:")
        print("---------------------------------------------------")
        

if __name__ == '__main__':
    financa_input = financeiro()
    financa_input.cadastrar()
    financa_input.imprima_inf()