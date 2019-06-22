n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

numbers = []
numbers.append(n1)
numbers.append(n2)
numbers.append(n3)
numbers.append(n4)
numbers.append(n5)
numbers.append(n6)

positives = 0
soma = 0

for number in numbers:
    if number > 0:
        positives = positives + 1
        soma = soma + number
media = soma/positives
print('{} valores positivos'.format(positives))
print('{:.1f}'.format(media))
