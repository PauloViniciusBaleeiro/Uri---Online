value = 0

a = 0 # álcool
g = 0 # gasolina
d = 0 # diesel

while value != 4:
  value = int(input())
  if value == 1:
    a += 1
  if value == 2:
    g += 1
  if value == 3:
    d += 1

print('MUITO OBRIGADO')
print('Alcool:', a)
print('Gasolina:', g)
print('Diesel:', d)
