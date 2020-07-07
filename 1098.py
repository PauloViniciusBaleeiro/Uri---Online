I = 0
J1 = 1
J2 = 2
J3 = 3

while (I <= 2):
    i = I
    print('variavel i', type(i))
    print(i)
    print('int', round(i, 1))
    if(type(i) == 'int'):
        print('inteiro')
        print('I={} J={}'.format(int(i), int(J1 + i)))
        print('I={} J={}'.format(int(i), int(J2 + i)))
        print('I={} J={}'.format(int(i), int(J3 + i)))
    else:
        print('I={:.1f} J={:.1f}'.format(i, (J1 + i)))
        print('I={:.1f} J={:.1f}'.format(i, (J2 + i)))
        print('I={:.1f} J={:.1f}'.format(i, (J3 + i)))
    I += 0.2
