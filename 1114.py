correctPass = 2002
check = False
result = []

while check == False:
  password = int(input())
  if(password == correctPass):
    check = True
    result.append("Acesso Permitido")
  else:
    result.append("Senha Invalida")

for r in result:
  print(r)