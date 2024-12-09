posição = 0

def fibonacci(posição):
    anterior = 1
    próximo = 1
    soma = 1
    for n in range(0,posição):
        print(anterior)
        soma= próximo + anterior
        anterior = próximo
        próximo = soma

while  posição != -99:
    print("Bem - Vindos À Sequência de Fibbonacci\n")
    print("-------------------------------")
    posição = int(input("Escolha uma posição:"))
    fibonacci(posição)