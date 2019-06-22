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

even = 0
odd = 0
positive = 0
negative = 0

for number in numbers:
    if (number % 2) == 0:
        even = even + 1
    else:
        odd = odd + 1 
    if (number > 0):
        positive = positive + 1
    elif(number < 0):
        negative = negative + 1

print('{} valor(es) par(es)'.format(even))
print('{} valor(es) impar(es)'.format(odd))
print('{} valor(es) positivo(s)'.format(positive))
print('{} valor(es) negativo(s)'.format(negative))
