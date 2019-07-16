number = int(input())

for i in range(number + 1):
    if i%2 == 0 and i > 0:
        result = i * i
        print('{}^2 = {}'.format(i, result))