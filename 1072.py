n1 = int(input())
numbers = []
for i in range(n1):
    i = int(input())
    numbers.append(i)

inside = 0
out = 0

for x in range(n1):
    if numbers[x] >= 10 and numbers[x] <= 20:
        inside = inside + 1
    else:
        out = out + 1

print('{}'.format(inside) + ' in')
print('{}'.format(out) + ' out')