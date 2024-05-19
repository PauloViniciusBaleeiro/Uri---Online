line = int(input())
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
  print(sum(matrix[line]))
else:
  print(sum(matrix[line])/12)
  