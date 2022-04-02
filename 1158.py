qty = int(input())

sums = []

for x in range(qty):
  numbers = input().split()
  n1 = int(numbers[0])
  n2 = int(numbers[1])
  sum = 0
  count = 0
  agg = 0
  while count < n2:
    check = (n1 + agg) % 2
    if check != 0 and count <= n2:
      sum = sum + n1 + agg
      count += 1
    agg = agg + 1
  sums.append(sum)
  
for n in sums:
  print(n)