final = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        final[0].append(n)
    elif n % 2 == 1:
        final[1].append(n)
final[0].sort()
final[1].sort()
print(f'Os números pares digitados foram: {final[0]}')
print(f'Os números impares digitados foram: {final[1]}')
