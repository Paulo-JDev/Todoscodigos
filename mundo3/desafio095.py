time = list()
joga = dict()
par = []

while True:
    joga.clear()
    joga['Jogador'] = str(input('Nome do jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {joga["Jogador"]} jogou: '))
    par.clear()
    for c in range(0, tot):
        par.append(int(input(f'Quantas gols na partida {c+1}? ')))
    joga['gols'] = par[:]
    joga['Total'] = sum(par)
    time.append(joga.copy())
    while True:
        rp = str(input('Quer continuar [S/N]: ')).strip().upper()
        if rp in 'NSsn':
            break
        print('ERRO! Responda somente com S ou N')
    if rp == 'N':
        break
print('-='*20)
print('cod ', end='')
for i in joga.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)