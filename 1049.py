info = input()
info1 = input()
info2 = input()

if (info == "vertebrado"):
    if (info1 == "ave"):
        if (info2 == "carnivoro"):
            print("aguia")
        elif (info2 == "onivoro"):
            print("pomba")
    elif (info1 == "mamifero"):
        if (info2 == "onivoro"):
            print("homem")
        elif (info2 == "herbivoro"):
            print("vaca")
elif (info == "invertebrado"):
    if (info1 == "inseto"):
        if (info2 == "hematofago"):
            print("pulga")
        elif(info2 == "herbivoro"):
            print("lagarta")
    elif (info1 == "anelideo"):
        if (info2 == "hematofago"):
            print("sanguessuga")
        elif (info2 == "onivoro"):
            print("minhoca")
