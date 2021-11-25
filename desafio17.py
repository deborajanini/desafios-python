#Desafio 17
#Débora Janini

numeros = input()

n1, n2, n3 = numeros.split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1>n2 and n1>n3 and n2>n3: 
    print(f'{n3}\n{n2}\n{n1}\n')
elif n1>n3 and n1>n2 and n3>n2:
    print (f"{n2}\n{n3}\n{n1}\n")
elif n2>n1 and n2>n3 and n1>n3:
    print (f"{n3}\n{n1}\n{n2}\n")
elif n2>n3 and n3>n1 and n2>n1:
    print (f"{n1}\n{n3}\n{n2}\n")
elif n3>n1 and n3>n2 and n1>n2:
    print (f"{n2}\n{n1}\n{n3}\n")
else:
    print (f"{n1}\n{n2}\n{n3}\n")


print(f'{n1}\n{n2}\n{n3}')
