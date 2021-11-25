#Desafio 27
#Débora Janini

quant_positivo = 0
soma = 0
for numeros in range(6):
    numero = float(input())
    if numero>0:
       quant_positivo += 1
       soma += numero
       media = soma/quant_positivo
       
print(quant_positivo, "valores positivos")
print(f"{media:.1f}")
