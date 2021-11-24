#Desafio 12 versão 3
#Débora Janini

#aqui tentarei usar eqquação dentro do for para economizar linha baseado em minhas colegas

#aqui declaro a entradad do valor
val = int(input())

#aqui crio uma lista das notas
minhasnotas = [100, 50, 20, 10, 5, 2, 1]


print (val)
#PARA CADA NOTA(faz papel de i, quantidade) NAS MINHAS NOTAS
#AQui ele faz os calculo de módulo/resto
#dentro do for até atingir a ultima nota

for nota in minhasnotas:
    print(f"{int(val / nota)} nota(s) de R$ {nota},00")
    val %= nota # %= - N = N % nota


"""
OUTRO MÉTDO PARA O FOR E UM POUCO MAIS COMPLEXO SERIA:

for NOTA in MINHASNOTAS:
  quant_notas = int(valor / minhasnotas)
  print("{} nota(s) de R$ {},00".format(quant_notas, notas))
  val -= quant_notas * nota # valor = valor -= quant_notas * nota
"""