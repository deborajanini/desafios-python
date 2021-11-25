#Desafio 18
#Débora Janini

"""

horarios = input()
H1 = int(horarios.split()[0])
H2 = int(horarios.split()[1])

eu tinha feito antes e funcionou:

horas = input()
hinit, hfinal = horas.split()
hinit=int(hinit)
hfinal=int(hfinal)
"""

hinit, hfinal = input().split()

hinit = int(hinit)
hfinal = int(hfinal)

if hfinal > hinit:
    tempo = hfinal - hinit
elif hinit == hfinal:
    tempo = 24
else:
    tempo = (24 - hinit) + hfinal

print(f"O JOGO DUROU {tempo} HORA(S)")



"""
O CÓDIGO PODERIA SER FEITO DA SEGUINTE MANEIRA TAMBÉM:

hi, hf = map(int, input().split()) DEFINE OS VALORES EM INT
EM ENTRADA SEPARADA
 O TEMPO É FINAL - INICIAL
t = hf - hi

SE O TEMṔO FOR NEGATIVO OU IGUAL A ZERO , ELE RECEBE UM NOVO VALOR
O ALOR CORRETO PARA O CALCULO
if t <= 0:
    t = t + 24

print(f'O JOGO DUROU {t} HORA(S)')
"""