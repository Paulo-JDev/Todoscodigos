import random
# Meu
""" alea = random.randint(0, 10)
print('\033[3;34;40mJOGO DE ADIVINHA 2.0\033[m')
print('\033[3;33mOBS: o numero não muda quando vc erra\033[m')
seu = int(input('Sou seu computador.... Adivinhe um numero entre 0 e 10: '))
tent = 0
while seu != alea:
    print('\033[1;31mVc errou\033[m')
    seu = int(input('Tente adivinhar novamente: '))
    tent += 1
if tent == 0:
    print('\033[1;32mVc acertou de primeira\033[m')
else:
    print('\033[1;32mParabens\033[m,Vc deu {} palpites até acertar'.format(tent)) """

# Do Professor
computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Séra que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('\033[1;31mMenos\033[m... Tente mais uma vezes')
        elif jogador < computador:
            print('\033[1;32mMais\033[m... Tente mais uma vezes')
print('Vc deu {} palpites para acertar. Parabens!'.format(palpites))
