#Desafio 28
#Débora Janini

N = int(input())

for numero in range(2, N+1, 2): #alcance de 2 a N+1 em passo de 2,
    # COMEÇA EM DOIS, PQ SE NÃO CoMEÇARIA EM 1 
    # e encerra em N+1 para incluir o N
    elevado_quadrado = numero**2
    print (f"{numero}^2 = {elevado_quadrado}")