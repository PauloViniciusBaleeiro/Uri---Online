import re

diaInicio = input()
h1 = input()
diaFim = input()
h2 = input()

#getting numbers
diaInicio =  int(re.sub('[^0-9]', '', diaInicio))
diaFim =  int(re.sub('[^0-9]', '', diaFim))
h1 = re.sub('[^0-9]', '', h1)
h2 = re.sub('[^0-9]', '', h2)

hh1 = int(h1[0]+h1[1])
mm1 = int(h1[2]+h1[3])
ss1 = int(h1[4]+h1[5])

hh2 = int(h2[0]+h2[1])
mm2 = int(h2[2]+h2[3])
ss2 = int(h2[4]+h2[5])

diffDay = diaFim - diaInicio
diffHour = hh2 - hh1
diffMin = mm2 - mm1
diffSec = ss2 - ss1

if diffHour < 0:
    diffDay = diffDay - 1
    diffHour = diffHour + 24

if diffMin < 0:
    diffHour = abs(diffHour) - 1
    diffMin = diffMin +60

if diffSec < 0:
    diffMin = abs(diffMin) - 1
    diffSec = diffSec + 60

print('{} dia(s)'.format(diffDay))
print('{} hora(s)'.format(diffHour))
print('{} minuto(s)'.format(diffMin))
print('{} segundo(s)'.format(diffSec))
