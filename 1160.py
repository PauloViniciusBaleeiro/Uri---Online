from math import floor

runs = int(input())

resps = []

def calcTime(pa, pb, ca, cb):
  count = 0
  while pa <= pb:
    count += 1
    pa = pa + int(floor(pa * (ca/100)))
    pb = pb + int(floor(pb * (cb/100)))
    if count > 100:
      return count
  return count

for n in range(runs):
  values = input().split()
  popA = int(values[0])
  popB = int(values[1])
  crescA = float(values[2])
  crescB = float(values[3])


  resps.append(calcTime(popA, popB, crescA, crescB))

for resp in resps:
  # print(resp)
  if resp <= 100:
    print(resp, 'anos.')
  else:
    print('Mais de 1 seculo.')

