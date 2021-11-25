#Desafio 16 versão 2
#Débora Janini
#Esta versão foi efita após estudar a vrsão da Adne usando função
#e serve maisapra aprendizagem

def notas(media): #aqui é definida uma função notas com o parâmetro media
    nota = float(input()) #aqui falo que a nota é uma entrada nessa função
    print("Nota do exame: {:.1f}".format(nota)) #esse print recebe o valor
    # de nota (format)

    media = (media+nota)/2 #aqui faço um cáluclo de media 
    #considerando o problema de recuperação
    #a media recebe o valor da media digitada e é atualizada caso 
    # #entre nessa função, como pode ser visto abaixo
    #a parti daqui, considerando a situação de em exame faço 
    #um if para os casos da recuperação

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media Final: {:.1f}".format(media)) 
    # aqui faz o print da média final, recebendo a media como valor

#aqui segue a lógica que fiz na versão 1
notasprovas = input()

n1, n2, n3, n4 = notasprovas.split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (2*n1 + 3*n2 + 4*n3+ n4)/10

#aqui se vê que a média recebe primeiro os valores das notas,
#para caso seja recuperação, entra na função



print("Media: {:.1f}".format(media)) 


if media >= 7:
        print("Aluno aprovado.")

elif media < 5:
    print("Aluno reprovado.")
#aqui entra a recuperação e o chamamento da função notas
#ao chamar a função notas, ele vai calcular a nova media
#e entra no if da função

else:
    print("Aluno em exame.")
    notas(media)