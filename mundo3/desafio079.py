valores = []
while True:
    n = int(input('Digite um valor: '))
    # n = int(input('Numero: '))
    #       if valores.count(n) == 0:
    #           valores.append(n)
    #       else:
    #           print('oud')
    if n not in valores:
        valores.append(n)
    else:
        print('valor dublicado! Não adicionado...')
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
    print('Valor adicionado com sucesso...')
valores.sort()
print(f'Vc digitou {valores}')
