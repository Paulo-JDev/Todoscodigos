val = []
t1 = []
l5 = []
while True:
    n = int(input('Digite um número: '))
    val.append(n)
    if t1.count(n) == 0:
        t1.append(n)
    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
t1.sort(reverse=True)
for pos, v in enumerate(val):
    if v == 5:
        l5.append(pos+1)
print(f'Foram digitados {len(val)} números')
print(f'Os valores em ordem decrescente(sem os repetidos) são:'
      f'\n{t1}')
if 5 in val:
    print(f'O valor 5 faz parte da lista\nnas posições {l5}')
else:
    print('O valor 5 não faz parte da lista')
