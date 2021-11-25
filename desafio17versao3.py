#Desafio 17
#Débora Janini
#Código feito pela Adne com modificações, 
#comentado por mim para compreensão da função map e sorted

"""
map() takes two arguments. The first one is the method
to apply, the second one is the data to apply it to. 
By this understanding, we can see this is doing nothing 
but typecasting every element of the list to an integer value. 
Since map returns the data type it was applied to, the list() 
method applied over map() is redundant. So now we have 
covered the following:
"""

linha = input() #declara uma entrada chamada linha
lista = (linha.strip().split()) #lista recebe a linha (enrtrada separada)
#o strip remove espaços antes e depois  da string

#UNico problema é'que tenho entradas infinitas se não der enter

lista = list(map(int, lista))

#AQUI O MAP DETERMNA QUE OS DADOS DA LISTA SÃO DO TIPO INTEIRO
#E LISTA RECEBE UMA LISTA COVERTIDA EM INTERIOS

listaordem = sorted(lista)

#aqui usou sortED ao invés de sort para definir o argumenot lista
#ou seja, a listaordem recebe lista em sequencia

"""
Creio qeu talvez poderia ter sido utilizado apeans lista.sort()
mas modificaria a lista, fazendo o pirnt final 
ser também em sequencia crescente (SIM, APÓS TESTAR FOI ISSO QUE ACONTECEU)
"""

#PAra i (item) na lista ordem (ordenada), imprima os itens (ja pula linha)
for item in listaordem:
    print(item)
print() #pula linha
for item in lista: #
    print(item)