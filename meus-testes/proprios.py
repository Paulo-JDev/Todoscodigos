print('=====================calculadora simples ======================')
print('soma = +\nsubtração = -\ndivisão = /\nmutiplicação = *')
num1 = float(input('Digite o primeiro numero: '))
ope = input('Digite um dos operadores que queira:')
num2 = float(input('Digite o segundo numero:'))
while True:
    if '+' == ope:
        print('O resultado foi: {:.2f}'.format(num1 + num2))
        break
    elif '-' == ope:
        print('O resultado foi: {:.2f}'.format(num1 - num2))
        break
    elif '/' == ope:
        print('O resultado foi: {:.2f}'.format(num1 / num2))
        break
    elif '*' == ope:
        print('O resultado foi: {:.2f}'.format(num1 * num2))
        break
print('fim da operação')
