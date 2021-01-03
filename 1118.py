new_media = 1

medias = []

def valida_valor(number):
    try:
        float(number)
    except:
        return False
    if float(number) < 0:
        return False
    if float(number) > 10:
        return False
    return True


while new_media == 1:
    notas = None
    nota1 = None
    nota2 = None

    while notas is None:
        valor = input()
        
        if valida_valor(valor):
            if nota1 is None:
                nota1 = float(valor)
            else:
                nota2 = float(valor)
        else:
            print('nota invalida')
        if (nota1 and nota2):
            notas = True
    
    media = (nota1 + nota2) / 2

    print('media = {0:.2f}'.format(round(media, 2)))

    print('novo calculo (1-sim 2-nao)')
    
    valid_option = None

    while valid_option is None:
        option = input()
        if (valida_valor(option)):
            if int(option) == 2:
                new_media = 2
                valid_option = True
            elif int(option) != 1:
                print('novo calculo (1-sim 2-nao)')
            else:
                valid_option = True
        else:
            print('novo calculo T (1-sim 2-nao)')
