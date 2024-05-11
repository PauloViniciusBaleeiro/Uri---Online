enter = float(input())
numbers = []
for x in range(100):
  if x > 0:
    numbers.append((numbers[x-1]/2))
  else:
    numbers.append(enter)
  
  print('N[{}] = {:.4f}'.format(x, numbers[x]))
  