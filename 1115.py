x = 1
y = 1
results = []

while x != 0 or y != 0:
  axis = input().split()
  x = int(axis[0])
  y = int(axis[1])

  if (x == 0 or y == 0):
    break
  elif (x > 0 and y > 0):
    results.append('primeiro')
  elif (x > 0 and y < 0):
    results.append('quarto')
  elif (x < 0 and y > 0):
    results.append('segundo')
  else:
    results.append('terceiro')

for result in results:
  print(result)