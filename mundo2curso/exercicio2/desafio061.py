print('10 termos de uma PA')
num = int(input('Digite um número: '))
r = int(input('A razão da P.A:'))
termo = num
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += r
    cont += 1
print('fim')
