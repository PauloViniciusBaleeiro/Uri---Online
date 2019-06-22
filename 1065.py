n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

numbers = []
numbers.append(n1)
numbers.append(n2)
numbers.append(n3)
numbers.append(n4)
numbers.append(n5)

pares = 0

for number in numbers:
    if (number % 2) == 0:
        pares = pares + 1 

print('{} valores pares'.format(pares))
