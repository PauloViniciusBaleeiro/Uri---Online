x = int(input())

z = int(input())

while z < x:
  z = int(input())

count = 1
n = x

while x < z:
  count = count + 1
  n = n + x
  print(n, z)
  if n > z:
    break

print(count)

