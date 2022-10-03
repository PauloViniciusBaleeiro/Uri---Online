numbers = []
for n in range(20):
  numbers.append(int(input()))
y = 0
for x in range(len(numbers) - 1, -1, -1):
  print('N[{}] = {}'.format(y, numbers[x]))
  y += 1
  