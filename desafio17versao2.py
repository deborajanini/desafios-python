#Desafio 17
#Débora Janini
#USAndo lista e sort - função que em regra coloca em ordem crescente

n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
seq = [n1, n2, n3] #aqui eu defino uma lista na ordem que o usuário entrou
seq.sort() #aqui a função sort coloca em ordem crescente (menor para maior)
#essa função pode ser usada de diversas formas, porém em regra em ascendente

#agora print a ordem depois do sort

print(seq[0])
print(seq[1])
print(seq[2])

print("")

#printa a ordem de entrada
print(n1)
print(n2)
print(n3)