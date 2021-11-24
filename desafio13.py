#Desafio 13
#Débora Janini

idade = int(input())

idadeAnos = idade//365
resto1 = idade%365

idadeMes = resto1//30
resto2 = resto1%30

idadeDias = resto2//1

print(f"{idadeAnos} ano(s)")
print(f"{idadeMes} mes(es)")
print(f"{idadeDias} dia(s)")