idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)
print()

idades = [idade1, idade2, idade3, idade4]
idades_num = [idade1, idade2, idade3, idade4]
idades.append(15)

for idade in idades:
    print(idade)

print()

for ida in range(1, 11):
    print(ida)

if 28 in idades:
    idades.remove(28)
else:
    print("Não foi possivel remover")

lista_numeros = [0, 26, 89, 90]

idades.append(lista_numeros)

print(idades)
print(idades[5][1])

numeros = [3, 5, 9, 12]
list = [39, 78, 48, 58]
lista = [39, 78, 48, 58, numeros]

idades.append(lista)

print(idades)
print(idades[6][0])
print(idades[6][4])
print(idades[6][4][3])

num = [9, 1]

num.extend(idades_num)
num.extend(lista_numeros)
num.extend(list)

print(num)
print()

lista_idade = [22, 36, 25, 14]
print(lista_idade)
print()

lista_idade_ano_que_vem = [(ida + 1) for ida in lista_idade]
print(lista_idade_ano_que_vem)

