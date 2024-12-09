nome_usuario = input("Digite seu nome: ")
senha = input("Crie uma Senha de acesso: ")
depósito = float(input("Quanto deseja depositar:"))
saque = str("Quanto deseja sacar:") 
global saldo 
saldo = depósito

print("*BEM-VINDO AO BANCO DO LEANDRO* ",saldo)
print("-------------------------------")
print(" 1- Extrato\n 2- Sacar\n 3- Depositar \n 0- SAIR \n")
print("-------------------------------")
opcao = input("Selecione uma opção:")

def sacar():
  global saldo
  saque = float(input("Quanto deseja sacar:"))
  saldo =  depósito - saque
  print (saldo)
  if saque > depósito :
   input("Saldo insulfisiente :(")
   

def depositar():
  global saldo
  print(f"SALDO {saldo}")
  novo_depósito = float(input("Quanto deseja depositar: "))
  saldo = saldo + novo_depósito
  print(f"SALDO ATUALIZADO {saldo}")

def extrato():
    global saldo
    extrato = input(f"Nome do Usuário:{nome_usuario}\n Saques Realizados:{saque}\n Depositos Realizados:{depósito}\n Saldo Total da Conta:{saldo}")

while opcao != "sair":
  if opcao != "sair":
    opcao = int(opcao)
    
  if opcao == 1 :
    extrato()
  elif opcao == 2:
    sacar()
  elif opcao == 3:
    depositar()
  elif opcao  == 0:
    input("OPEREÇÃO FINALIZADA....")
  else :
    input("Opção inexistente!!!")
    
 


