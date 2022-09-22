inputs = []
def vetor(entrada, idx):
  valor = 1
  if entrada > 0:
    valor = entrada
  inputs.append('X[{}] = {}'.format(idx, valor))

for i in range(10):
  num = int(input())
  vetor(num, i)
  
print(*inputs, sep='\n')