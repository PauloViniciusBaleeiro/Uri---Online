numbers = []
for i in range(100):
  num = input()
  if (float(num) <= 10):
    numbers.append([i,float(num)])

for n in numbers:
  print('A[{}] = {}'.format(n[0], n[1]))