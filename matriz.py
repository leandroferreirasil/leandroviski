import random

#matriz = [[0 for _ in range(3)] for _ in range(111)]
matriz = [[0,0,0],[0,0,0],[0,0,0]]
print(matriz)

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = random.randint(0,50)
        
matriz[1][1] = 999
matriz[2][2] = "FIMMMMMMMMMMMMM"

print(matriz)