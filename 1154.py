num = int(input())

sum = 0
count = 0
if num > 0:
  sum = num
while num > 0:
  num = int(input()) 
  if num > 0:
    sum += num
  count += 1

calc = sum/count
print("{0:.2f}".format(round(calc, 2)))