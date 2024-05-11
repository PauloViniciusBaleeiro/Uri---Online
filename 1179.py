numbers = []
for n in range(15):
  numbers.append(int(input()))

oddNumbers = []
evenNumbers = []

def isEven(num):
  return num % 2 == 0

for x in range(len(numbers)):
  if isEven(numbers[x]):
    evenNumbers.append(numbers[x])
  else:
    oddNumbers.append(numbers[x])

  if len(evenNumbers) == 5:
    for e in range(len(evenNumbers)):
      print('par[{}] = {}'.format(e, evenNumbers[e]))
    evenNumbers = []
  if len(oddNumbers) == 5:
    for o in range(len(oddNumbers)):
      print('impar[{}] = {}'.format(o, oddNumbers[o]))
    oddNumbers = []
  
for y in range(len(oddNumbers)):
  print('impar[{}] = {}'.format(y, oddNumbers[y]))

for z in range(len(evenNumbers)):
  print('par[{}] = {}'.format(z, evenNumbers[z]))
