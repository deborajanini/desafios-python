#Desafio 11
#Débora Janini
""" VOU DESENVOLVER O CÓDIGO DE DUAS FORMAS
A SEGUNDA VAI ESTAR COMENTADA LINHA A LINHA
PARA NÃO ATRAPALHAR AO RODAR """

"""Eu quero 3 entradas para cada peça,
sendo que cada peça tenha uma mesma linha"""

linhap1 = input().split() #aqui falo que a linhap1 é uma entrada que vai ser dividida (split)

cp1 = int(linhap1[0]) #aqui falo que cp1 recebe um inteiro na primeira posição de linhap1
np1 = int(linhap1[1]) #np1 é inteiro e está na segunda posição
vp1 = float(linhap1[2]) #vp1 é flaot e está na terceira posição

#agora vou fazer o mesmo para p produto 2 (p2)


print("VALOR A PAGAR: R$ %.2f"%VP)

linhap2 = input().split()

cp2 = int(linhap2[0])
np2 = int(linhap2[1])
vp2 = float(linhap2[2])

valorFinal = np1*vp1 + np2*vp2

#print('VALOR A PAGAR: R$ = ', f'{(valorFianl):.2f}')
print (f"VALOR A PAGAR: R$ %.2f" % (valorFinal))

##SEGUNDA FORMA##


#linhap1 = input().split(" ") #o espaço dentro das aspas indica a oq considrar padrão para a separação do split
#linhap2 = input().split(" ") 

#cp1,np1,vp1 = linhap1 #aqui fala quais saõ as entradas em ordem do split
#cp2,np2,vp2 = linhap2

#valorFinal = (int(np1) * float(vp1)) + (int(np2) * float(vp2)) #aqui eu declaro os tipos de entrada para naõ dar porblema depois

#print('VALOR A PAGAR: R$ = ', f'{(valorFianl):.2f}')
