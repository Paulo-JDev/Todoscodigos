tot = 0
num = int(input('Digite um número:'))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;34m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}\033[m'.format(c), end=' ')
print('\nO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('\nE por isso ele é \033[1;32mPRIMO\033[m')
else:
    print('por isso ele não é \033[1mPRIMO\033[m')
