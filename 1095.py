I = 1
J = 60

for x in range(13):
    if J == 60:
        print('I={}'.format(I) + ' J={}'.format(J))
        I = I + 3
        J = J - 5
    else:
        print('I={}'.format(I) + ' J={}'.format(J))
        I = I + 3
        J = J - 5
