#Desafio 20
#Débora Janini

salario= float(input())

if salario >=0 and salario <=400:
    percent= 0.15

elif salario <=800:
    percent= 0.12
    
elif salario <=1200:
    percent= 0.10    
    
elif salario <=2000:
    percent= 0.07     
    
else:
    percent= (0.04)     
    
   
nsalario = salario + (percent*salario)
reajuste = nsalario - salario


print(f"Novo salario: {nsalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual:", int(percent*100), "%")