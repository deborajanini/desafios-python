#Desafio 34
#Débora Janini

senha = 2002
senha_digitada = int(input())

while senha != senha_digitada:
    print ('Senha invalida')
    senha_digitada = int(input())
print('Acesso permitido')