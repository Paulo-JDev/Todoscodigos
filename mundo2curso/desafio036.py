print('\033[4;36m financiamento da sua casa com empréstimo bancário \033[m')
tst = 1000 / 100 * 30
valor1 = float(input('Valor da casa:'))
valor2 = float(input('Seu salario atual:'))
valor3 = int(input('Quantos anos de financiamento:'))
mesano = valor1 / (valor3 * 12)
calc = valor2 / 100 * 30
if calc < mesano:
    print('Seu emprestimo foi negado.\nPara ser aprovado, uma parcela não pode exeder a 30% do seu salario\n'
          'Sendo 30% R$\033[1;32m{:.2f}\033[m e a parcela R$\033[1;33m{:.2f}\033[m,'
          'assim exedendo R$\033[1;31m{:.2f}\033[m'
          .format(calc, mesano, mesano - calc))
elif calc >= mesano:
    print('Seu emprestimo foi aprovado')
    print('pois o valor da parcela é inferior a 30% do seu salario\n'
          '\033[4;36minformação\033[m: sua porcentagem de 30%: R${:.0f}\n'
          '\033[4;36minformação\033[m: valor da parcela: R${:.0f}'.format(calc, mesano))

