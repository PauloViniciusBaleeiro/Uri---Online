entrada = int(input())

doubles = entrada

for i in range(10):
  if i > 0:
    doubles = doubles * 2
  print('N[{}] = {}'.format(i, doubles))