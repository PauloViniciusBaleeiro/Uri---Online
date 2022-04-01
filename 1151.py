num = int(input())

while (num >= 46 or num <= 0):
  num = int(input())

fibonacci = [0, 1]
count = 2

if num == 1:
  print(0)
elif num == 2:
  print(fibonacci[0], fibonacci[1])
else:
  while count < num:
    sum = fibonacci[count-2] + fibonacci[count-1]
    fibonacci.append(sum)
    count = count + 1

  for i in range(len(fibonacci)):
    if (i < (len(fibonacci)-1)):
      print(fibonacci[i], end = ' ')
    else:
      print(fibonacci[i])
