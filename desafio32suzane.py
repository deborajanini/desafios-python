#Desafio 32 verao Suzane
#Comentado por Débora Janini
"""
eu uso o comando de map pra poder encontrar um vencedor, 
e lá no finalzinho no print eu defino que a primeira 
chave do map é o que o sheldon jogou
e a segunda chave é o que o raj jogou.

as três primeiras linhas do meu código eu coloquei uma 
letra pra definir aqueles resultados. mas foi mais pra facilitar 
e não ter que ficar escrevendo várias vezes

dai pra incluir todas as possibilidades de disputa, 
pra isso eu precisei colocar cada 
uma das opções que o primeiro jogador poderia ter colocado
"""
b= 'Bazinga!'
t= 'Raj trapaceou!!'
e= 'De novo!'
#map é o dicionário
#usou dicionário dentro de dicionário
map_to_winner = {
  'pedra': {
    'pedra': e,
    'papel': t,
    'tesoura': b,
    'lagarto': b,
    'Spock': t,
  },
  'papel': {
    'pedra': b,
    'papel': e,
    'tesoura': t,
    'lagarto': t,
    'Spock': b,
  },
  'tesoura': {
    'pedra': t,
    'papel': b,
    'tesoura': e,
    'lagarto': b,
    'Spock': t,
  },
  'lagarto': {
    'pedra': t,
    'papel': b,
    'tesoura': t,
    'lagarto': e,
    'Spock': b,
  },
  'Spock': {
    'pedra': b,
    'papel': t,
    'tesoura': b,
    'lagarto': t,
    'Spock': e,
  },
}
quantidade = int(input())

for index, valor in enumerate(range(quantidade)):#enumerar a quantidade casoa a caso
    #for indice, valor in enumarate (lista ou no caso N)
    sheldon, raj = input().split()
    #imprime o caso +1 para não dar zero
    #e  chama o dicionário para comparar as entradas
    print(f'Caso #{index+1}: {map_to_winner[sheldon][raj]}')