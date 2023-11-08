print('Sequencia de Fibonacci')
qnt = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} > {}'.format(t1, t2), end='')
while cont <= qnt:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > Fim')
