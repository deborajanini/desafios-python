#Desafio 29
#Debora Janini

quant_notas = 0
soma = 0

while quant_notas < 2:
    nota = float(input())
    if (nota>10) or (nota<0):
        print ('nota invalida')
    else:
        quant_notas = quant_notas + 1
        soma += nota
media = soma/ 2
print(f'media = {media:.2f}')
#print (f"media = %.2f" % (MEDIA))