print('Aumento salarial')
sala = float(input('Digite seu salario:'))
if sala >= 1250:
    print('Com um aumento de 10%, seu novo salario será de R${:.2f}'.format((sala/100) * 10 + sala))
else:
    print('Com um aumento de 15%, seu novo salario será de R${:.2f}'.format((sala/100) * 15 + sala))
