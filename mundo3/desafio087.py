matx = [[], [], []]
somap = treso = 0
for l in range(0, 3):
    for i in range(0, 3):
        matx[l].append(int(input(f'Digite um valor em [{l},{i}]: ')))
print('-='*20)
for l in range(0, 3):
    for i in range(0, 3):
        print(f'[{matx[l][i]:^5}]', end='')
    print()
for li in matx:
    for pi in li:
        if pi % 2 == 0:
            somap += pi
print('-='*20)
print(f'A soma dos pares digitados foram: {somap}')
for l in range(0, 3):
    treso += matx[l][2]
print(f'A soma total da 3 coluna foi de: {treso}')
print(f'O maior valor da 2 coluna foi: {max(matx[1])}')
