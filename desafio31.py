#Desafio 31
#Débora

N = int(input()) #entro com a minha quantidade 
array = [] #aqui abro meu array que ainda está vazio

array = list(map(int, input().split())) #aqui meu array recebe em
#tipo lista todas as entradas separadas por espaço (split)
#do tipo interiro tbm(int/map)

#para cada numero eu tenho que verificar se ele é menor que o menor

menor = array[0] #o menor começa sendo o primeiro numero entrado
posic = 0 #a psoição tbm começa em zero

for indice_numero in range(N): #pq eu quero na quantidade da entrada N
    if array[indice_numero]< menor:
        menor = array[indice_numero]
        posic = indice_numero

print("Menor valor:", menor)
print("Posicao:", posic)