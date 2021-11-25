#Desafio 23
#Débora Janini

salario = float(input())

if salario <= 2000.00:
    print('Isento')
    
elif salario <= 3000.00:
    valor = salario - 2000
    imp8 = valor * 0.08
    print(f"R$ %.2f" %(imp8))

elif salario <= 4500.00:
    valor = salario - 3000
    imp8 = 1000 * 0.08
    imp18 = (valor * 0.18) + imp8
    print(f"R$ %.2f" %(imp18))
    
else:
    valor = salario - 4500
    imp8 = 1000 * 0.08
    imp18 = 1500 * 0.18
    imp28 = (valor * 0.28) + imp8 + imp18
    print(f"R$ %.2f" %(imp28))