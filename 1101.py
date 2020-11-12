x = 1
y = 1
result = []
numberdict = []
while x > 0 and y > 0:
    
  numbers = input().split()
  x = int(numbers[0])
  y = int(numbers[1])
  numberdict.append(numbers)

  if (x < y):
    soma = 0
    seq = []
    for i in range(x,y+1):
      seq.append(i)
      soma += i
  else:
    soma = 0
    seq = []
    for i in range(y,x+1):
      seq.append(i)
      soma += i

  resSum = 'Sum=' + str(soma)
  seq.append(resSum)
  result.append(seq)
del result[-1]
for r in result:
  print (*r)
  