import random
from time import sleep
print('\033[4;33mJogo de Jokempô\033[m')
esc = str(input('Escolha: pedra, papel ou tesoura?')).strip().lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
lst = ['pedra', 'papel', 'tesoura']
mistu = random.choice(lst)
print('Eu joguei {}'.format(mistu))
if esc == mistu:
    print('\033[1;34mDeu empate\033[m')
elif esc == 'pedra' and mistu == 'tesoura':
    print('\033[1;32mParabens\033[m, pedra ganha de tesoura')
elif esc == 'papel' and mistu == 'pedra':
    print('Você \033[1;32mganhou\033[m, papel ganha de pedra')
elif esc == 'tesoura' and mistu == 'papel':
    print('Você \033[1;32mganhou\033[m, tesoura ganha de papel')
else:
    print('{} perde pra {}\nVocê \033[1;31mperdeu\033[m'.format(esc, mistu))
