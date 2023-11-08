print('Status do IMC')
peso = float(input('Qual é o seu peso?'))
alt = float(input('Qual é a sua altura?'))
imc = peso / alt ** 2
print('{:.2f}'.format(imc))
if imc < 18.5:
    print('IMC baixo')
elif imc < 25:
    print('IMC ideal')
elif imc < 30:
    print('Você esta sobrepeso')
elif imc < 40:
    print('Você tem Obesidade')
else:
    print('Você tem Obesidade mórbida')
