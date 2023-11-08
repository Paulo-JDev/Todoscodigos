print('PALÍTROMOS')
fra = str(input('Digite uma frase: ')).strip().lower()
f = fra.split()
junt = ''.join(f)
inver = ''
for li in range(len(junt) - 1, -1, -1):
    inver += junt[li]
print(f'A frase {fra}\nde traz pra frente fica {inver}')
if junt == inver:
    print('A frase é um Palídromo')
else:
    print('A frase não é um Palídromo')
