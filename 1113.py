x = 1
y = 2

result = []
numberDict = []

while x != y:
  numbers = input().split()
  x = int(numbers[0])
  y = int(numbers[1])
  numberDict.append(numbers)

  if(x < y):
    result.append("Crescente")
  elif (y < x):
    result.append("Decrescente")
  else:
    break

for r in result:
  print(r)
