value1 = int(input())
value2 = int(input())

if value1 < value2:
  v1 = value1
  v2 = value2
else:
  v1 = value2
  v2 = value1
  
sum = 0
for x in range(v1, (v2+1)):
  if (x % 13) != 0:
    sum += x

print(sum)
