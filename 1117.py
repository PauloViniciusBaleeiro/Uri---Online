valid = False

results = []
media = []

while valid == False:
  grade = float(input())
  if(grade < 0 or grade > 10):
    results.append('nota invalida')
  else:
    media.append(grade)

  if(len(media) == 2):
    valid = True
    break

calc = ((media[0] + media[1])/2)
results.append('media = {0:.2f}'.format(round(calc, 2)))

for result in results:
  print(result)