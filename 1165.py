qty = int(input())
resultados = []

def ehPrimo(entrada):
  soma = 0
  for i in range(entrada + 1):
    if i == 0:
      continue
    if entrada % i == 0:
      soma += 1
  if soma > 2:
    resultados.append('{} nao eh primo'.format(entrada))
  else: 
    resultados.append('{} eh primo'.format(entrada))

for i in range(qty):
  num = int(input())
  ehPrimo(num)

print(*resultados, sep='\n')
