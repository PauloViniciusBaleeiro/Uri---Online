num = int(input())

fat = num
mul = 1

for x in range(1, num):
  fat = fat * mul
  mul = num - x


print(fat)