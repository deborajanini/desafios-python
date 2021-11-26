#Desafio 31
#Débora Janini
#Este desafio fiz com base em de duas colegas, 
#aonde pude ver ferraemntas novas do python e entender


N = int(input())
array = list(map(int, input().split()))

menor = min(array) #min retorna o menor
posicao = array.index(menor) #index retorna o indice, então
#index do menor valor no array
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')