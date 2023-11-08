valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
mai = max(valores)
man = min(valores)
print(f'Você digitou os valores: {valores}')
print(f'O menor valor digitado foi o {man} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == mai:
        print(f'{pos}...', end='')
print(f'\nO maior valor digitado foi o {mai} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == man:
        print(f'{pos}...', end='')
