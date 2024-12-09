class Tour:
    def __init__(self, nivel ="", mobilidade ="",horas= 0 , digite = 0, hora_inicial = 0 , hora_final = 0, local= ""):
        self._nivel         =   nivel
        self._mobilidade    =   mobilidade
        self._hora_inicial  =   hora_inicial
        self._hora_final    =   hora_final
        self._local         =   local
        self._horas         =   horas
        self._digite        =   digite

    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_mobilidade(self):
        return self._mobilidade
    
    def set_mobilidade(self, mobilidade):
        self._mobilidade = mobilidade

    def get_horas(self):
        return self._horas
    
    def set_horas(self, horas):
        self._horas = horas

    def get_hora_inicial(self):
        return self._hora_inicial
    
    def set_hora_inicial(self, hora_inicial):
        self._hora_inicial = hora_inicial

    def get_hora_final(self):
        return self._hora_final
    
    def set_hora_final(self, hora_final):
        self._hora_final = hora_final

    def get_local(self):
        return self._local
    
    def set_local(self, local):
        self._local = local

    def cadastrar(self):
        print("  SEJA BEM VINDO!!!!!\n Cadastre Aqui sua Mobilidade>>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n")
        self._nivel                = input("Digite seu nivel:")
        self._mobilidade           = input("Qual melhor mobiidade para seu Tour?:")
        self._hora_inicial         = int(input("Que horário deseja começar seu Tour?:"))
        self._hora_final           = int(input("Que horário deseja finalizar seu Tour?:"))
        self._local                = input("Onde será o local da entrega?:")
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
        self._nivel         =   ""
        self._mobilidade    =   ""
        self._hora_inicial  =   0
        self._hora_final    =   0
        self._local         =   ""
        self._horas         =   0
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
        print("---------------------------------------------------")
        print(f"  {self._nivel}\n Mobilidade Solicitada:{self._mobilidade}\n Ínicio do Tour:{self._hora_inicial}\n Fim do Tour: {self._hora_final}\n Tempo de Uso:{self._horas} hrs \n Local para Entrega:{self._local}")
     
    def tempo_tour(self):
        self.set_horas(self.get_hora_final() - self.get_hora_inicial())
        self.imprima_inf()
        
        

if __name__ == '__main__':
    tour_input = Tour()
    tour_input.cadastrar()
    tour_input.tempo_tour()
    tour_input.imprima_inf()