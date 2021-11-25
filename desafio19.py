#Desafio 19
#Débora Janini

h1, m1, h2, m2 = input().split()

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

inicio = (h1*60)+m1
fim = (h2*60)+m2
tempoEmMinutos = fim- inicio

if (tempoEmMinutos <= 0):
    tempoEmMinutos += 1440

horas = tempoEmMinutos//60
minutos = tempoEmMinutos%60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")