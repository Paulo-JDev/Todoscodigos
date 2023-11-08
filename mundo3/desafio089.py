print('-='*15)
print(f'{"NOTAS":^30}')
print('-='*15)
ficha = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], med])
    r = str(input('Quer continuar [S/N]: ')).strip().upper()
    if r in 'Nn':
        break
print('-='*15)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('_'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    op = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
print('<<<< VOLTE SEMPRE >>>>')
