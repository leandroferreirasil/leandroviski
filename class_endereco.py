class endereco:
    def __init__(self, nivel = 0, rua ="", numero = 0 , digite= 0, bairro = ""):
        self._nivel  =    nivel
        self._rua    =    rua
        self._numero =    numero
        self._bairro =    bairro
        self._digite =    digite

    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_rua(self):
        return self._rua
    
    def set_rua(self, rua):
        self._rua = rua

    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero

    def get_bairro(self):
        return self._bairro
    
    def set_bairro(self, bairro):
        self._bairro = bairro

    def cadastrar(self):
        print("  SEJA BEM VINDO!!!!!\n Cadastre Aqui Seu Endereço>>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n")
        self._nivel  = int(input("Digite seu nivel:"))
        self._rua    = input("Digite o nome da sua Rua:")
        self._numero = input("Digite o número da sua Casa:")
        self._bairro = input("digite seu Bairro:")

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
        self._nivel  =    0
        self._rua    =    ""
        self._numero =    ""
        self._bairro =    ""
        self._digite =    ""
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
        
        print(f" SEU ENDEREÇO!!!\n Rua:{self._rua} \n Número da Casa:{self._numero} Bairro: {self._bairro}")
        print("---------------------------------------------------")
        
        

if __name__ == '__main__':
    endereco_input = endereco()
    endereco_input.cadastrar()
    endereco_input.imprima_inf()
    