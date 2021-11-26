#Desafio 35
#Débora Janini

pares = input()

n1, n2 = pares.split()

n1 = int(n1)
n2 = int(n2)

while n1 != n2:
    if n1 > n2:
        print('Decrescente')
    else:
        print('Crescente')
    n1, n2 = list(map(int, input().split())) #isso aqui é a mesma entrada
    #que de cima, em uma só linha