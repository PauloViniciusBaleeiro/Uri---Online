enter = int(input())
numbers = []
for x in range(1000):
  v = 0
  while v < enter:
    numbers.append(v)
    v = v + 1
    
  print('N[{}] = {}'.format(x,numbers[x]))