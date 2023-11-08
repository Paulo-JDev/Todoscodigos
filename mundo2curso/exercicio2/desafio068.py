import random
v = 0
print('-'*30)
print('   VAMOS JOGAR PAR OU IMPAR')
print('-'*30)
while True:
    player = int(input('Diga um valor: '))
    comp = random.randint(0, 10)
    soma = player + comp
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    print(f'VC jogou {player} é o computador {comp}. total de {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Vc PERDEU!!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('VC PERDEU!!')
            break
    print('Vamos jogar novamente.....')
print('GAME OVER! Você venceu {} vezes'.format(v))
