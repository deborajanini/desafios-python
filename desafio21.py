#Desafio 21
#Débora Janini

pal1 = str(input())
pal2 = str(input())
pal3 = str(input())

if pal1 == 'vertebrado':
    if pal2 == 'ave':
        if pal3 == 'onivoro':
            print ("pomba")
        else:
            print ("aguia")
    else:
        if pal3 == 'onivoro':
            print ("homem")
        else:
            print ("vaca")
else:
    if pal2 == 'inseto':
        if pal3 == "hematofago":
            print ("pulga")
        else:
            print ("lagarta")
    else:
        if pal3 == 'hematofago':
            print ("sanguessuga")
        else:
            print ("minhoca")