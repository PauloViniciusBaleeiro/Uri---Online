numbers = input().split()


def horas(numbers):
    if (int(numbers[2]) == int(numbers[0])):
        if (int(numbers[3]) > int(numbers[1])):
            valor = 0
            return str(valor)
        else:
            valor = 23
            return str(valor)


    elif (int(numbers[2]) < int(numbers[0])):
        if (int(numbers[3]) < int(numbers[1])):
            valor = (int(numbers[2]) + 24) - int(numbers[0])
            return str(valor - 1)

        else:
            valor = (int(numbers[2]) + 24) - int(numbers[0])
            return str(valor)      
    
    else:
        if (int(numbers[3]) < int(numbers[1])):
            valor = 0
        
        else:
            valor = int(numbers[2]) - int(numbers[0])
        return str(valor)

def minutos(numbers):
    if (int(numbers[3]) < int(numbers[1])):
        valor = (int(numbers[3]) + 60) - int(numbers[1])
        return str(valor)
    
    else:
        valor = int(numbers[3]) - int(numbers[1])
        return str(valor)


if (int(numbers[0]) == int(numbers[1]) and int(numbers[2]) == int(numbers[3]) and int(numbers[0]) == int(numbers[2])):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

else:
    print('O JOGO DUROU ' + horas(numbers) + ' HORA(S) E ' + minutos(numbers) + ' MINUTO(S)')
