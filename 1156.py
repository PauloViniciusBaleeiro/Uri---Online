s = 0
d = 1
dv = 1

while d <= 39:
  s += d/dv
  d = d + 2
  dv = dv * 2

print("{0:.2f}".format(round(s, 2)))