final = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    if len(final) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    final.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar [S/N]:')).strip().upper()
    if r in 'Nn':
        break
print('-='*20)
print(f'Ao todo, foram cadastradas {len(final)} pessoas')
print(f'O maior peso foi {mai}Kg ', end='')
for p in final:
    if p[1] == mai:
        print(p[0], end=' ')
print()
print(f'O menor peso foi {men} ', end='')
for nome, p in final:
    if p == men:
        print(f'{nome}', end=' ')
