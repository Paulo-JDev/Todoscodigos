""" t = list()
t.append('Paulo')
t.append(25)
g = list()
g.append(t[:])
t[0] = 'joao'
t[1] = 12
g.append(t[:])
print(g)
# ==========================================================
pes = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pes)
print(pes[1])
print(pes[0][0])
print(pes[2][1])
for p in pes:
    print(f'{p[0]} tem {p[1]} anos')"""
# =========================================================
galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for g in galera:
    if g[1] >= 21:
        print(f'{g[0]} é maior de idade')
        totmai += 1
    else:
        totmen += 1
        print(f'{g[0]} é menor de idade')
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
