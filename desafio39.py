#Desafio 39
#Débora JAnini


#casos = int(input())


#for i in range(casos): #descobrir a posicao
 #   texto_orig = input().split() #lista de letras
 #   texto2 = '' #recebe o texto

  #  for letra in texto_orig: #procura os espacos na lista
   #     if letra != '': #espaco
    #        texto2 += letra[0] #armazena primeira letra
    #print(f'{texto2}')



N = int(input())

for i in range(N):
	texto = input().split(" ")
	texto2 = []
	texto3 = []
	for x in texto:
		if x != "":
			texto2.append(x)

	for y in texto2:
		texto3.append(y[0])
	print(''.join(texto3))