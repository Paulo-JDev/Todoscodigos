fut = {}
par = []
fut['Jogador'] = str(input('Nome do jogador: ')).strip().title()
tot = int(input(f'Quantas partidas {fut["Jogador"]} jogou: '))
for c in range(0, tot):
    par.append(int(input(f'Quantas gols na partida {c+1}? ')))
fut['gols'] = par[:]
fut['Total'] = sum(par)
print('-='*20)
print(f'O jogador {fut["Jogador"]} jogou {fut["Partidas"]} partidas')
for i, v in enumerate(fut['gols']):
    print(f'=> Na partida {i+1}, faz {v} gols.')
print(f'Foi um total de {fut["Total"]} gols')
