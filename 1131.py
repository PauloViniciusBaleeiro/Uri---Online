matches = 0
inter = 0
gremio = 0
ties = 0
new_game = 0

def setValues(results, inter, gremio, ties, matches):
  if results[0] > results[1]:
    inter += 1
  elif results[0] < results[1]:
    gremio += 1
  else:
    ties += 0

  matches += 1

  return [inter, gremio, ties, matches]

def checkNewGame(value):
  if value != 1 and value != 2:
    print('Opção inválida')
    return False
  else:
    return True


while new_game <= 1:
  result = input().split()

  values = setValues(result, inter, gremio, ties, matches)
  inter = values[0] 
  gremio = values[1]
  ties = values[2]
  matches = values[3]

  print('Novo grenal (1-sim 2-nao)')
  new_game = int(input())
  checkOption = checkNewGame(new_game)
  if checkOption:
    if new_game == 2:
      break


print(matches, 'grenais')
print('Inter:{0}'.format(inter))
print('Gremio:{0}'.format(gremio))
print('Empates:{0}'.format(ties))
if gremio > inter:
  print('Gremio venceu mais')
elif gremio < inter:
  print('Inter venceu mais')
else:
  print('Nao houve vencedor')
