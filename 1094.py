import operator
from functools import reduce
n = int(input())

coelhos = []
ratos = []
sapos = []
lista = []

def somaLista(lista):
    resultado = reduce(operator.add, lista)
    return resultado

def total():
    total = somaLista(coelhos) + somaLista(ratos) + somaLista(sapos)
    return total

def percentual(valor):
    resultado = valor/total()
    return resultado

def classificaLista(registro):
    if registro[1] == 'C':
        coelhos.append(int(registro[0]))
    if registro[1] == 'R':
        ratos.append(int(registro[0]))
    if registro[1] == 'S':
        sapos.append(int(registro[0]))
    

for n in range(n):
    linha = input().split()
    lista.append(linha)
    
for x in lista:
    classificaLista(x)


print('Total: {} '.format(total()) + 'cobaias')
print('Total de coelhos: {}'.format(somaLista(coelhos)))
print('Total de ratos: {}'.format(somaLista(ratos)))
print('Total de sapos: {}'.format(somaLista(sapos)))
print('Percentual de coelhos: {:.2f} '.format(percentual(somaLista(coelhos))*100) + '%')
print('Percentual de ratos: {:.2f} '.format(percentual(somaLista(ratos))*100) + '%')
print('Percentual de sapos: {:.2f} '.format(percentual(somaLista(sapos))*100) + '%')
print('')