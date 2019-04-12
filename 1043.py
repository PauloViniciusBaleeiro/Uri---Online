
numbers = input().split()

a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])

if (abs(b - c) < a and a < (b + c)):
    print('Perimetro =', (a + b + c))
    
elif (abs(a - c) < b and b < (a + c)):
    print('Perimetro =', (a + b + c))

elif (abs(a - b) < c and c < (a + b)):
    print('Perimetro =', (a + b + c))

else:
    print('Area =', (a + b)/2*c)
