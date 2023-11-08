temp = {}
dados = []
tot = idato = 0
while True:
    temp['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        temp['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if temp['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    temp['Idade'] = int(input('Idade: '))
    dados.append(temp.copy())  # USAR A PO*** DO COPY
    tot += 1
    idato += temp['Idade']
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
        if resp in 'NnSs':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break
média = idato / tot
print(f'- O total de pessoas: {tot}')  # OU usar o LEN(). Ex: len(final)
print(f'- A média da idade do grupo é {média:.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for c in dados:
    if c['Sexo'] in 'Ff':
        print(c['Nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for c in dados:
    if c['Idade'] > média:
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
