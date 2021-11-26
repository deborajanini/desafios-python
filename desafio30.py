#Desafio 30
#Débora Janini

#montado meu array por lista

lista = []
#Eu queor uma entrada de 10 com quebra

for indice in range(10):
    x = int(input()) #aqui vou fazer minha entrada até ter 10 valores
    lista.append(x) #adiciono cada x na lista
    if lista[indice] <=0 :
        lista[indice] = 1
    print(f"X[{indice}] = {lista[indice]}")

"""
OUTRA FORMA:



for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    print(f'X[{i}] = {x}')
"""
