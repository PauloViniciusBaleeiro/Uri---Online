qty = int(input())
resultados = []

def ehPerfeito(entrada):
  soma = 0
  for i in range(entrada):
    if i == 0:
      continue
    if entrada % i == 0:
      soma += i
  if soma == entrada:
    resultados.append('{} eh perfeito'.format(entrada))
  else: 
    resultados.append('{} nao eh perfeito'.format(entrada))

for i in range(qty):
  num = int(input())
  ehPerfeito(num)

print(*resultados, sep='\n')
