#Desafio 25
#Débora Janini

positivo = 0
for numeros in range(6):
    numero = float(input())
    if numero>0:
       positivo += 1
print(positivo, "valores positivos")
