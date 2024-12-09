def menu():
 print("-------------------------------")
 print(f"*BEM-VINDO AO BANCO DO Lêlê* ")
 print(f"Usuário *{nome_usuario}*","Disponível R$",saldo)
 print("-------------------------------")
 print(" 1- Extrato\n 2- Sacar\n 3- Depositar\n 0- SAIR \n")
 print("-------------------------------")

nome_usuario = input("Por favor, Digite seu NOME: ")
senha = input("Digite sua SENHA: ")
depósito = float(input("Quanto deseja depositar: R$"))
print("ATENÇÃO!!!\nSolicite Extrato somente no fim da operação:) ")
saque = str("Quanto deseja sacar: R$") 
global saldo 
saldo = depósito
global novo_depósito
novo_depósito = depósito
menu()
opcao = input(f"Escolha uma opção *{nome_usuario}*:")

  

def sacar():
  global saldo
  global saque
  print("ATENÇÃO! Somente 1 Saque Diário...")
  saque = float(input("Quanto deseja sacar: R$"))

  if saque > saldo :
    print ("Saldo Atual R$",saldo)
    print("....................................")
    print(f"Saque de R${saque} ,Não Realizado:(")
    print("Saldo insulfisiente :(")
  else:
    saldo = saldo - saque 
    print ("Saldo Atual R$",saldo)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Saque de R${saque} ,relizado com sucesso!!!")


def extrato():
  global saldo
  global saque
  global novo_depósito
  print(f"Nome do Usuário:*{nome_usuario}*\n ltimo Saque:R${saque}\n Depositos inicial:R${depósito}\n DepósitoS Recente:R${novo_depósito} \n Saldo Atual:R${saldo}")

def depositar():
  global saldo
  global novo_depósito
  print(f"SALDO R${saldo}")
  print("ATENÇÃO! Somente 1 Depósito Diário...")
  novo_depósito = float(input("Quanto deseja depositar:R$"))
  saldo = saldo + novo_depósito
  print(f"SALDO ATUALIZADO R${saldo}")


while opcao != "sair":
  if opcao != "sair":
    opcao = int(opcao)
    
  if opcao == 1 :
   extrato()
   menu()
   opcao = input(f"Escolha uma opção *{nome_usuario}*:")
   
  elif opcao == 2:
    sacar()
    menu()
    opcao = input(f"Escolha uma opção *{nome_usuario}*:")
    
  elif opcao == 3:
    depositar()
    menu()
    opcao = input(f"Escolha uma opção *{nome_usuario}*:")
  elif opcao  == 0:
    input("OPEREÇÃO FINALIZADA....")
  else :
    input("Opção inexistente!!!")
    menu()
    opcao = input(f"Escolha uma opção *{nome_usuario}*:")
    
    