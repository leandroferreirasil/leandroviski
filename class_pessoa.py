class pessoa:
    def __init__(self, nome ="", email ="", Cpf = "", nome_de_usuário ="",digite=0, senha= "", telefone = "", habilitação ="", nivel = 0 , tipo_nivel ="", Rg = "", tipagem = ""):
        self._nome               =   nome
        self._email              =   email
        self._Cpf                =   Cpf
        self._nome_de_usuário    =   nome_de_usuário
        self._senha              =   senha
        self._telefone           =   telefone
        self._habilitação        =   habilitação
        self._nivel              =   nivel
        self._tipo_nivel         =   tipo_nivel
        self._Rg                 =   Rg
        self._tipagem            =   tipagem
        self._digite             =   digite
        

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_nome_usuário(self):
        return self._nome_usuário
    
    def set_nome_usuário(self, nome_usuário):
        self._nome_usuário = nome_usuário

    def get_senha(self):
        return self._senha
    
    def set_senha(self, senha):
        self._senha= senha

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email

    def get_telefone(self):
        return self._telefone
    
    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_habilitação(self):
        return self._habilitação
    
    def set_habilitação(self, habilitação):
        self._habilitação = habilitação

    def get_Cpf(self):
        return self._Cpf
    
    def set_Cpf(self, Cpf):
        self._Cpf = Cpf

    def get_rg(self):
        return self._rg
    
    def set_rg(self, rg):
        self._rg = rg
    
    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    

    def cadastrar(self):
        
        print("  SEJA BEM VINDO!!!!!\n Cadastre-se Aqui>>>>>")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("NÍVEL>>>\n 1-Cliente\n 2-Fornecedor\n 3-Funcionario\n 4-Gerencia\n 5-Motorista\n 6-Entregador\n")
        self._nivel = int(input("Digite seu nivel:"))
        self._nome = input("Digite seu nome:")
        self._email = input("Digite seu email:")
        self._Cpf = input("Digite seu CPF:")
        self._nome_usuário = input("Crie um nome de usuário :")
        self._senha = input("Crie uma senha\n(Obrigatório conter letras números e simbolos):")
        self._telefone = input("Digite seu telefone:")
        self._habilitacao = input("Possui CNH ?(s/n)")
        self._Rg = input("Digite seu RG:")
        
    
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
        print(f" Nome:{self._nome} \n Email:{self._email}\n Nome de usuário: {self._nome_de_usuário}\n Telefone:{self._telefone}\n Cpf: {self._Cpf}\n Tem CNH:{self._habilitação}\n Rg:{self._Rg}")
        
   

        



        
        
        
        

if __name__ == '__main__':
    pessoa_input = pessoa()
    pessoa_input.cadastrar()
    pessoa_input.funcao()
    pessoa_input.verificar_nivel()
    

    
 