#Desafio 12 versão 2
#Débora Janini
#Versão com divisão e lista e for

#aqui eu tenho uma lista com todas as minhas notas em string
minhasnotas = ['100,00', '50,00', '20,00', '10,00', '5,00', '2,00', '1,00']

#aqui inicio uma lista
listanotas = []

#aqui faço a entrada do valor inteiro
val = int(input())
VAL = val

#o append adiccina um item a lista

listanotas.append(val//100) #adiciono a lista a quantidade de notas de 100
val = val - listanotas[0] * 100 #redefino o val com o valor que sobrou

listanotas.append(val//50)
val = val - listanotas[1]* 50

listanotas.append(val//20)
val = val - listanotas[2]*20

listanotas.append(val//10)
val = val - listanotas[3] * 10

listanotas.append(val//5)
val = val - listanotas[4]* 5

listanotas.append(val//2)
val = val - listanotas[5] * 2

listanotas.append(val//1)


#agora PARA cada um dos 7 eu impromo VAL, que é p primeiro valor
#deposi printo os valores seguintes, varaindo i (quantidade)
print(VAL)
for i in range(7):

    print(listanotas[i], "nota(s) de R$", minhasnotas[i])