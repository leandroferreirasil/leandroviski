nome= input("Digite o nome do aluno:")
notas =[]

notas.append(7.5)
notas.append(8.5)
notas.append(3.5)
print(notas)
print(len(notas))

notas.append(9.3)
print(notas)
print(len(notas))
notas.append(255.90)

print(notas)
print(len(notas))

notas.pop()
print(notas)

notas.pop(0)
print(notas)
print(len(notas))
notas[0] = 9.1
print(notas)

print(len(notas))