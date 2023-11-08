num = int(input('Digite um numero inteiro:'))
result = num % 2
if result == 0:
    print('{} É um numero \033[1;34mPar \033[m'.format(num))
else:
    print('{} É um numero \033[1;33mImpar \033[m'.format(num))
