print("\033[1;32mTabuada 2.0\033[m")
num = int(input('Digite um valor:'))
for t in range(1, 11):
    tab = t * num
    print('{} X {} = {}'.format(num, t, tab))
print('Fim')
