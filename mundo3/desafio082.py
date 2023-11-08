v1 = list()
lispr = list()
lisip = list()
while True:
    n = int(input('Digite um valor: '))
    v1.append(n)
    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
for pi in v1:
    if pi % 2 == 0:
        lispr.append(pi)
    elif pi % 2 == 1:
        lisip.append(pi)
print(f'A lista completa: {v1}')
print(f'Lista de Pares: {lispr}')
print(f'Lista de Impares: {lisip}')
