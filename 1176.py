entradas = int(input())

def fibonnacci_calc(number):
  if number == 0:
    print('Fib({}) = {}'.format(number, 0))
  elif number == 1:
    print('Fib({}) = {}'.format(number, 1))
  else:
    fibo = [0,1]
    for x in range(number + 1):
      if(x > 1):
        fibo.append(fibo[x-2] + fibo[x-1])
    # print(fibo)
    print('Fib({}) = {}'.format(number, fibo[number]))

numeros = []

for i in range(entradas):
  numeros.append(int(input()))

for n in numeros:
  fibonnacci_calc(n)
