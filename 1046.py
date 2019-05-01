numbers = input().split()

if (int(numbers[0]) == int(numbers[1])):
    print('O JOGO DUROU 24 HORA(S)')

elif (int(numbers[1]) < int(numbers[0])):
    valor = (int(numbers[1]) + 24) - int(numbers[0])
    print('O JOGO DUROU ' + str(valor) + ' HORA(S)')

else:
    valor = int(numbers[1]) - int(numbers[0])
    print('O JOGO DUROU ' + str(valor) + ' HORA(S)')
