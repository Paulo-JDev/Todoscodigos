num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
esc = int(input('Escolha de 0 a 20, e veja ele por extenso: '))
while esc > 20 or esc < 0:
    print('Tente novamente.', end=' ')
    esc = int(input('Escolha de 0 a 20, e veja ele por extenso: '))
print(f'Você escolheu o número {num[esc]}')
