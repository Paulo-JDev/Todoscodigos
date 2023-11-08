print('10 termos de uma PA')
num = int(input('Digite um número: '))
r = int(input('A razão da P.A:'))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos mais você quer mostrar a mais? '))
soma = total + mais
print('A progressão foi finalizada com {} termos mostrados'.format(soma))
