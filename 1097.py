I = 1
J = 7
count = 1

while (I <= 9):
    print('I={} J={}'.format(I,J))
    # print("J-count", J-count)
    # print('J', J)
    # print('count',count)
    if ((J-count) == 2):
        I = I + 2
        J = J + 4
        count = count - 1
    # elif (J == 8):
    #     break
    else:
        J = J - 1 
    count = count + 1