import operator
from functools import reduce


for x in range(100):
    n = int(input())    
    if x == 0 :
        maior = n
        posicao = x + 1
    elif x > 0 and n > maior:
        maior = n
        posicao = x + 1

print(maior)
print(posicao)