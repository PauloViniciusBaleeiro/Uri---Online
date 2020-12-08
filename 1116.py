qtd = int(input())

results = []
dividendo = []
divisor = []

for num in range(qtd):
  numbers = input().split()
  dividendo.append(int(numbers[0]))
  divisor.append(int(numbers[1]))

  if(divisor[num] == 0):
    results.append('divisao impossivel')
  else:
    results.append(dividendo[num]/divisor[num])

for result in results:
  print(result)