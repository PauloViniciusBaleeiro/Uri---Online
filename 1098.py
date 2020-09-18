I = 0
J1 = 1
J2 = 2
J3 = 3
x = 0

# print('i =>', I)

while (I <= 2):
    i = I
    # print('x%5', x%5 == 0)
    # print('x', x)
    if(x==0 or (x%5 == 0)):
        # print('inteiro')
        print('I={} J={}'.format(int(round(i)), int(round(J1 + i))))
        print('I={} J={}'.format(int(round(i)), int(round(J2 + i))))
        print('I={} J={}'.format(int(round(i)), int(round(J3 + i))))
    else:
        print('I={:.1f} J={:.1f}'.format(i, (J1 + i)))
        print('I={:.1f} J={:.1f}'.format(i, (J2 + i)))
        print('I={:.1f} J={:.1f}'.format(i, (J3 + i)))
    x += 1
    # print('x%5', x)
    I += 0.2
