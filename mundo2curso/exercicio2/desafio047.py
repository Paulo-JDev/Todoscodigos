print("Numero pares entre 1 a 50")
for c in range(2, 51, 2):
    print(c, end=' ')
print('FIM')

""" Resolução do prof """

for p in range(1, 51):
    if p % 2 == 0:
        print(p, end=' ')
print('Acabou')
