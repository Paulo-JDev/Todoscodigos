from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
rank = list()
for c, v in jogo.items():
    sleep(0.6)
    print(f'{c} tirou {v} no dado')
print('-='*30)
print('  == PLACAR DOS JOGADORES ==')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(rank):
    print(f'    {c+1}º lugar: {v[0]} com {v[1]}')  # AltGr + tecla perto do enter.
    sleep(0.6)
