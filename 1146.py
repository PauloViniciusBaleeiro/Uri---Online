qty = 2

while qty > 0:
  qty = int(input())
  numbers = []
  for x in range (1, qty + 1):
    numbers.append(x)
  if len(numbers) > 0:
    print(*numbers)
