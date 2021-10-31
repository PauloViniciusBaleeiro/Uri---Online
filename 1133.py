num1 = int(input())
num2 = int(input())

if num1 > num2 :
  temp = num1
  num1 = num2
  num2 = temp


for x in range((num1 + 1), num2):
  if (x % 5) == 2:
    print(x)
  if (x % 5) == 3:
    print(x)
