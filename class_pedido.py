class pedido:
    def __init__(self, nivel = 0, car_mobil ="", classe = "" , digite = 0,especificacoes = "", quantidade ="" ):
       self._nivel              =   nivel
       self._car_mobil          =   car_mobil
       self._classe             =   classe
       self._especificacoes     =   especificacoes
       self._quantidade         =   quantidade
       self._digite             =   digite

    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_car_mobil(self):
        return self._car_mobil
    
    def set_car_mobil(self, car_mobil):
        self._car_mobil = car_mobil

    def get_classe(self):
        return self._classe
    
    def set_classe(self, classe):
        self._classe = classe

    def get_especificacoes(self):
        return self._especificacoes
    
    def set_especificacoes(self, especificacoes):
        self._especificacoes = especificacoes

    def get_quantidade(self):
        return self._quantidade
    
    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def cadastrar(self):
        print("  SEJA BEM VINDO!!!!!\n Cadastre Dados da sua pedido>>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n") 
        self._nivel          = int(input("Digite seu nivel:"))
        self._car_mobil         = input("Qual automóvel deseja?:")
        self._classe         = input("Digite a classe do seu veículo\n(Classe econômica - executiva - gold):")
        self._especificacoes            = input("Digite as especificações do veículo:")
        self._quantidade           = input("Digite Quantas pessoas cabem no veículo :")

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

    def funcao(self):
        print("---------------------------------------------------")
        print(" DIGITE 1 PARA \n >>ATUALIZAR\n DIGITE 2 PARA \n >>IMPRIMIR OS DADOS ")
        self._digite = int(input(":"))
        
        if self._digite == 1:
            self.cadastrar()

    
        else:
            self.verificar_nivel()

            

       
       

    def imprima_inf(self):
        
        print(f" TUDO SOBRE SEU PEDIDO!!!\n Automóvel:{self._car_mobil} \n Classe:{self._classe}\n Específicações: {self._especificacoes}\n Quantas pessoas suporta: {self._quantidade}")
        print("---------------------------------------------------")
        
        

if __name__ == '__main__':
    pedido_input = pedido()
    pedido_input.cadastrar()
    pedido_input.verificar_nivel()
    