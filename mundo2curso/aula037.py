print('Conversor de digitos')
num = int(input('Digite um numero inteiro: '))
print('Escolha uma das basses para conversão:'
      '\n[ 1 ] conversor para BINARIO'
      '\n[ 2 ] conversor para  OCTAL'
      '\n[ 3 ] conversor para HEXADECIMAL')
op = int(input('Sua opção:'))
if op == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Este valor não existe, tente novamente')
