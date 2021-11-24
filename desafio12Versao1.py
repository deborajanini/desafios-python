#Desafio 12 Versão1
#Débora Janini

#AQui vou tentar fazer por meio de divisões interiras

val = int(input())
print(val)
nota1 = val // 100  #Primeiro divido a quantidade pelas notas de 100, que é o maior valor
val = val - nota1*100 #aqui redefino valor com o que sobrou

nota2 = val // 50
val = val - nota2*50

nota3 = val // 20
val = val - nota3*20

nota4 = val // 10
val = val - nota4*10

nota5 = val // 5
val = val - nota5*5

nota6 = val // 2
val = val - nota6*2

nota7 = val // 1
val = val - nota7*1

print('%i nota(s) de R$ 100,00'%nota1) #%i indica a quantidade
print('%i nota(s) de R$ 50,00'%nota2)
print('%i nota(s) de R$ 20,00'%nota3)
print('%i nota(s) de R$ 10,00'%nota4)
print('%i nota(s) de R$ 5,00'%nota5)
print('%i nota(s) de R$ 2,00'%nota6)
print('%i nota(s) de R$ 1,00'%nota7)

