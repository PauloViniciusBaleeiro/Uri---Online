I = 0
J = 1

while (I <= 2):
    print('I={:.1f} J={}'.format(I,J))
    if ((J - I) == 3):
        I = I + 0.2
        J = 1 + I
    else:
        J = int(J) 
        J = J + I + 1 
    