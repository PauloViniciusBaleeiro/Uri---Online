numbers = input().split()
s_numbers = []
for number in numbers:
    s_numbers.append(float(number))
s_numbers = sorted(s_numbers)

def tri(a, b, c):
    ret = False
    if (a >= (b+c)):
        res = "NAO FORMA TRIANGULO"
        tipos.append(res)
        ret = True
    return ret

def ret(a, b, c):
    if (a**2 == (c**2 + b**2)):
        res = "TRIANGULO RETANGULO"
        tipos.append(res)

def obt(a, b, c):
    if ((a**2) > (c**2 + b**2)):
        res = "TRIANGULO OBTUSANGULO "
        tipos.append(res)

def acu(a, b, c):
    if ((a**2) < (c**2 + b**2)):
        res = "TRIANGULO ACUTANGULO "
        tipos.append(res)

def equ(a, b, c):
    if (a == b and b == c):
        res = "TRIANGULO EQUILATERO "
        tipos.append(res)

def iso (a, b, c):
    if (a == b and a != c and b != c):
        res = "TRIANGULO ISOSCELES "
        tipos.append(res)
    
    elif (a == c and a != b and c != b):
        res = "TRIANGULO ISOSCELES "
        tipos.append(res)
    if (c == b and b != a and c != a):
        res = "TRIANGULO ISOSCELES "
        tipos.append(res)

def check(a, b, c):
    res = tri(a, b, c)
    if (res):
        for tipo in tipos:
            print(tipo)
    else:
        ret(a, b, c)
        obt(a, b, c)
        acu(a, b, c)
        equ(a, b, c)
        iso(a, b, c)
        for tipo in tipos:
            print(tipo)

a = float(s_numbers[2])
b = float(s_numbers[1])
c = float(s_numbers[0])
tipos = []

check(a, b, c)
