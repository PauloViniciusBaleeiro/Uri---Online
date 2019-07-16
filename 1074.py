n = int(input())
numbers = []
for i in range(n):
    i = int(input())
    numbers.append(i)

for x in numbers:
    if x == 0:
        print('NULL')
    elif x < 0:
        if abs(x) % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    else:
        if x % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')