qtd = int(input())
i = 0

while (i < qtd):
  if(i == qtd):
    break
  num = input().split()
  x = int(num[0])
  y = int(num[1])
  
  if (x < y):
    soma = 0
    for num in range(x,y):
      num += 1
      if (num % 2 == 1 and num != y):
        soma += num
    
    print(soma)
  else:
    soma = 0
    for num in range(y,x):
      num += 1
      if (num%2 == 1 and num != x):
        soma += num
    print(soma)
  i += 1
