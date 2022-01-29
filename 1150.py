numX = int(input())
numY = int(input())

while numY <= numX:
  numY = int(input())

count = 2
aux = 1
sum = numX

while sum <= numY:
  sum = sum + (numX + aux)
  
  if sum <= numY:
    count = count + 1
    aux = aux + 1


print (count)