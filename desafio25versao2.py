#Desafio 25 versão 2
#Débora Janini

numeros =1
positivo = 0

while numeros <=6:
    num = float(input())
    if num >0:
        positivo +=1
    numeros +=1
print (positivo, "numeros positivos")
