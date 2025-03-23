col = int(input())
operation = str(input())
matrix = []
for n in range(144):
  for x in range(12):
    lineMatrix = []
    for y in range(12):
      lineMatrix.append(float(input()))
    matrix.append(lineMatrix)
  break

if(operation == 'S'):
  sum = 0
  for x in matrix:
    sum += x[col]
  print(sum)
else:
  sum = 0
  for x in matrix:
    sum += x[col]
  print(round(sum/12, 1))