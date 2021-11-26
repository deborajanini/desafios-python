#Desafio 40
#Débora JAnini

#o try except é utilizado para evitar erros e tentar fazer
#mesmo que esteja errado, o except é para caso esteja errado

while True: #enquanto isso for verdadeiro, tente
    try:
        senha = input() 
        quantidade_caract = len(senha)
        maiuscula = False
        minuscula = False
        num = False
        if ((quantidade_caract > 32) or (quantidade_caract < 6)):
            print('Senha invalida.')
        else:
            for i in range(quantidade_caract):
                if senha[i].isupper(): #isupper = se tem maiscula
                    maiuscula = True
                elif senha[i].islower(): #islower = se tem minuscula
                    minuscula = True

                #a função ord retorna um inteiro que representa
                # um caractere Unicode, aí eu usei os caracteres da tabela Ascii
                elif(((ord(senha[i]))>47) and ((ord(senha[i]))<58)):
                    num = True
                else:
                    maiuscula = False
                    break
            if (maiuscula and minuscula and num):
                print('Senha valida.')
            else:
                print('Senha invalida.')
            
    except EOFError:
        break