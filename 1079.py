import operator
from functools import reduce

n = int(input())
medias = []


def atribuiPeso(lista):
    novaLista = []
    for x in range(len(lista)):
        if x == 0:
            n = lista[x] * 2
        elif x == 1:
            n = lista[x] * 3
        else:
            n = lista[x] * 5
        novaLista.append(n)
    return novaLista

def converteFloat(lista):
    novaLista = []
    for x in lista:
        novaLista.append(float(x))
    return novaLista

def somaLista(lista):
    newLista = reduce(operator.add, atribuiPeso(converteFloat(lista)))
    return newLista

def calculaMedia(lista):
    soma = somaLista(lista)
    media = soma/10
    return media

def imprimeResultados(lista):
    for x in lista:
        print('{:.1f}'.format(x))

for x in range(n):
    numbers = input().split()
    media = calculaMedia(numbers)
    medias.append(media)
    
imprimeResultados(medias)






# for x in range(n):
#     if sum > 0:
#         sums.append(sum)
#         sum = 0
#     for i in range(3):
#         number = float(input())
#         if i == 0:
#             numbers.append(number * 2)
#             sum = sum + numbers[i]
#         elif i == 1:
#             numbers.append(number * 3)
#             sum = sum + numbers[i]
#         else:
#             numbers.append(number * 5)
#             sum = sum + numbers[i]
#         sums.append(sum)
# for x in range(n):
#     print('{:.1f}'.format(sums[2]/10))

