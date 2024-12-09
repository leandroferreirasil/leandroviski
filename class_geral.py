# gestao.py
from class_pessoa import pessoa
from class_endereco import endereco
from class_cidade import cidade
from class_habilitacao import cnh
from class_Tour import Tour
from class_pedido import pedido
from class_financeiro import financeiro

# Aqui é a classe que gerencia tudo

   


# Bloco principal que cria as instâncias e executa a gestão
if __name__ == '__main__':
    # Instanciando as classes com alguns dados de exemplo
    pessoa_input = pessoa()
    pessoa_input.cadastrar()
    pessoa_input.funcao()
    pessoa_input.verificar_nivel()
    endereco_input = endereco()
    endereco_input.cadastrar()
    endereco_input.funcao()
    endereco_input.verificar_nivel()
    cidade_input = cidade() 
    cidade_input.cadastrar()
    cidade_input.funcao()
    cidade_input.verificar_nivel()
    cnh_input = cnh()
    cnh_input.cadastrar()
    cnh_input.funcao()
    cnh_input.verificar_nivel()
    tour_input = Tour()
    tour_input.cadastrar()
    tour_input.funcao()
    tour_input.tempo_tour()
    tour_input.verificar_nivel()
    pedido_input = pedido()
    pedido_input.cadastrar()
    pedido_input.funcao()
    pedido_input.verificar_nivel()
    financa_input = financeiro()
    financa_input.cadastrar()
    financa_input.funcao()
    financa_input.verificar_nivel()