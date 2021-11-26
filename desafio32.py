#Desafio 38
#Débora Janini

num_jogos = int(input()) #quantidade de jogos

for i in range(num_jogos):
    sheldon, raj = input().split()

    if sheldon == raj:
        print(f"Caso #{i+1}: De novo!")
    else: #primeiro sheldon ganhaa e depois raj
        if ((sheldon =="pedra" and (raj =="lagarto" or raj=="tesoura")) or (sheldon =="papel" and (raj =="pedra" or raj=="Spock")) or (sheldon =="tesoura" and (raj =="papel" or raj=="lagarto")) or (sheldon =="lagarto" and (raj =="Spock" or raj=="papel")) or (sheldon =="Spock" and (raj =="tesoura" or raj=="pedra"))):
            print(f"Caso #{i+1}: Bazinga!")
        elif ((raj =="pedra" and (sheldon =="lagarto" or sheldon=="tesoura")) or (raj =="papel" and (sheldon =="pedra" or sheldon=="Spock")) or (raj =="tesoura" and (sheldon =="papel" or sheldon=="lagarto")) or (raj =="lagarto" and (sheldon =="Spock" or sheldon=="papel")) or (raj =="Spock" and (sheldon =="tesoura" or sheldon=="pedra"))):
            print(f"Caso #{i+1}: Raj trapaceou!")