operation = str(input())
matrix = []
for n in range(144):
  for x in range(12):
    lineMatrix = []
    for y in range(12):
      lineMatrix.append(float(input()))
    matrix.append(lineMatrix)
  break

 
totalSum = 0
divisor = 0

# for i in range(12):
#     for j in range(i + 1, i):
#         print('j, i', i, j)
#         totalSum += matrix[i][j]
#         divisor += 1
for i in range(12):
    for j in range(12):
        if i + j > 11:
            totalSum += matrix[i][j]
            divisor += 1

if(operation == 'S'):
  print(totalSum)
else:
  print(round(totalSum/divisor, 1))
