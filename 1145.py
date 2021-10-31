numbers = input().split()

qty = int(numbers[0])
max_range = int(numbers[1])
max_range += 1

current_value = 0
while current_value < max_range - 1:
  num = []
  for y in range(qty):
    if current_value >= max_range -1:
      break    
    current_value += 1
    num.append(current_value)
  current_value + qty
  print(*num)
