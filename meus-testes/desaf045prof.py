import random
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é sua jogada?'))
print('=' * 22)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=' * 22)
if computador == 0:
    print('o')
elif computador == 1:
    print('p')
elif computador == 2:
    print('e')
