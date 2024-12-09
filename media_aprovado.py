print("CALCULANDO A MÉDIA DO ALUNO :")
print("------------------------------")
nome =str(input("Digite o nome do aluno: "))
nota_1=float(input("\nDigite a nota_1: "))
nota_2= float(input("\nDigite a nota_2: "))
nota_3= float(input("\nDigite a nota_3: "))
nota_4= float(input("\nDigite a nota_4: "))

media =(int (nota_1 + nota_2 + nota_3 + nota_4) / 4 )
print ( nome,"FICOU:", media,"de MÉDIA")
print(f"As notas do aluno foram :{nota_1, nota_2, nota_3, nota_4} e a média ficou {media}")

if  media >= 7.0:
 print(f"O Aluno {nome} está aprovado!")
elif media >= 5.0 :
 print(f"O Aluno {nome} está em recuperação!")
else:
 print(f" O Aluno {nome} está reprovado")
   
  
  