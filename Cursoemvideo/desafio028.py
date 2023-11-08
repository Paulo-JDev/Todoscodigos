import random
print('tente adivinhar qual o numero que caiu, entre 0 a 5)')
seu = int(input('Digite o numero que acha:'))
alea = random.randint(0, 5)
if seu == alea:
    print('Parabens, vc ganhou')
else:
    print('Vc perdeu, eu pensei no {} e não no {}'.format(alea, seu))
