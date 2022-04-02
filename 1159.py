n = int(input())

sums = []

while n != 0:  
  sum = 0
  count = 0
  agg = 0
  while count < 5:
    check = (n + agg) % 2
    if check == 0 and count < 5:
      sum = sum + n + agg
      count += 1
    agg = agg + 1
  sums.append(sum)
  n = int(input())
  
for n in sums:
  print(n)