numbers = input().split()

a = float(numbers[0])
b = float(numbers[1])

if (a%b == 0 or b%a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
