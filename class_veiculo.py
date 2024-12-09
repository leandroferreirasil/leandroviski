class Veiculo:
    def __init__(self, nome):
        self.nome = nome

class Acelerar(Veiculo):
    def acelerar(self):
        print(f"{self.nome} está acelerando.")

class Trocando(Veiculo):
    def trocando(self):
        print(f"{self.nome} está mudando de marcha.")

class Frear(Veiculo):
    def frear(self):
        print(f"{self.nome} está freando,.")

class Reduzindo(Veiculo):
    def reduzindo(self):
        print(f"{self.nome} está reduzindo marcha.")

class Ligar(Veiculo):
    def ligar(self):
        print(f"{self.nome} está ligado.")

class Businar(Veiculo):
    def buzinando(self):
        print(f"{self.nome} está buzinando.")

class Tocar(Veiculo):
    def tocar(self):
        print(f"{self.nome} está com o som ligado")

class Limpar(Veiculo):
    def limpa(self):
        print(f"Começou a chover {self.nome} está com o parabrisas ligado e funcionando")

class Desligar(Veiculo):
    def desligar(self):
         print(f"{self.nome} está desligado")

class Moto( Businar, Desligar, Tocar, Ligar,Acelerar,Limpar,Trocando,Frear,Reduzindo):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)   
            
class Caminhao( Businar, Desligar, Ligar, Tocar,Limpar,Acelerar,Trocando,Frear,Reduzindo):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)   
    
    def caga_molhado(self):
        print(f"{self.nome} está cagando molhado no quintal!!!!")

class Onibus( Desligar, Tocar, Ligar, Businar,Limpar, Acelerar,Trocando,Frear,Reduzindo):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)   
    
    def peida(self):
        print(f"{self.nome} está peidando!")

class Aviao( Desligar, Tocar,Ligar, Businar,Limpar, Acelerar,Trocando, Frear,Reduzindo):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)   

class Jetski( Desligar, Tocar,Ligar,Businar, Limpar, Acelerar,Trocando,Frear, Reduzindo):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)   

class Lancha( Desligar, Tocar,Ligar,Businar,Limpar,Acelerar,Trocando,Frear,Reduzindo):
    def __init__(self, nome):
        Veiculo.__init__(self, nome)   




if __name__ == "__main__":
    moto = Moto("Yamaha")
    moto.ligar()
    moto.acelerar()        
    moto.tocar()       
    moto.buzinando()
    moto.trocando()
    moto.limpa()
    moto.frear()
    moto.reduzindo() 
    moto.desligar()
    caminhao = Caminhao("Mercedes Benz")
    caminhao.ligar() 
    caminhao.acelerar()      
    caminhao.tocar()   
    caminhao.buzinando()
    caminhao.trocando()
    caminhao.limpa()
    caminhao.frear()
    caminhao.reduzindo()
    caminhao.desligar()    
    onibus = Onibus("Marcopolo")
    onibus.ligar()
    onibus.acelerar()
    onibus.tocar()       
    onibus.buzinando()
    onibus.trocando()
    onibus.limpa()
    onibus.frear()
    onibus.reduzindo()        
    onibus.desligar() 
    onibus.limpa()  
    aviao = Aviao("Voo 280")
    aviao.ligar() 
    aviao.acelerar()      
    aviao.tocar()
    aviao.buzinando()
    aviao.trocando()
    aviao.limpa()
    aviao.frear()
    aviao.reduzindo()
    aviao.desligar()
    jetski = Jetski("Kavasakiski")
    jetski.ligar()
    jetski.acelerar()        
    jetski.tocar()       
    jetski.buzinando() 
    jetski.trocando()
    jetski.limpa()
    jetski.frear()
    jetski.reduzindo()
    jetski.desligar() 
    lancha = Lancha("Fishinlauch")
    lancha.ligar()
    lancha.acelerar()        
    lancha.tocar()       
    lancha.buzinando() 
    lancha.trocando()
    lancha.limpa()
    lancha.frear()
    lancha.reduzindo()
    lancha.desligar() 
        