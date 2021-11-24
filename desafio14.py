#Desafio 14
#Débora Janini
numero = float(input())

if float(0 <= numero <= 25):
    print("Intervalo [0,25]")
elif float(25 < numero <= 50):
    print("Intervalo (25,50]")
elif float(50 < numero <= 75):
    print("Intervalo (50,75]")
elif float(75 < numero <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
