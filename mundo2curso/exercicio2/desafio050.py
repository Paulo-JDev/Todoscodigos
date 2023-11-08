s = 0
for c in range(1, 7):
    num = int(input('Digite um numero:'))
    calc = num % 2
    if calc == 0:
        s = s + num
print('A soma de cada numero par foi de {}'.format(s))
