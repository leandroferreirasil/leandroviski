
notas =[]

def ler_nota():
  notas.append(float(input("Digite uma nota: ")))

def calcular_media():
    somatorio =sum(notas)
    quantidade_elementos = len(notas)
    media = somatorio / quantidade_elementos
    print("Média :",round(media,2))

ler_nota()
ler_nota()
ler_nota()
ler_nota()
calcular_media()
print("Maior nota:",max(notas))
print("Menor nota:",min(notas))