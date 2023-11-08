matx = [[], [], []]
for c in range(0, 3):
    for p in range(0, 3):
        matx[c].append(int(input(f'Digite um valor para [{c},{p}]: ')))
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matx[c][p]:^5}]', end='')
    print()

#  =================DO PROFESSOR===================
"""matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para [{c},{i}]:'))
print('-='*30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()"""
