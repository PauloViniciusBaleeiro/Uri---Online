ent = int(input())
numbers = input()
numbers = numbers.split()

for i in range(len(numbers)):
  numbers[i] = int(numbers[i])

menor = numbers[0]
pos = 0
for x in range(1, len(numbers)):
  if numbers[x] < menor:
    menor = numbers[x]
    pos = x

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(pos))
