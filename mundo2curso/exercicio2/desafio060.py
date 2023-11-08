le = 1
esc = int(input('\033[0;36mDigite um valor e descubra seu Fatorial:\033[m '))
for c in range(1, esc + 1):
    if c == 1:
        print('\033[1;34m{}!\033[m = {}'.format(esc, c), end='')
    else:
        print(' X {}'.format(c), end='')
    le *= c
print(' = \033[1;32m{}\033[m'.format(le))


n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
