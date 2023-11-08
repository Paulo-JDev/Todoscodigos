print('Aumento de 15% no seu salário')
s1 = float(input('digite seu salário atual:R$'))
alm = (s1 * 15)/100
s2 = alm + s1
print('Seu novo salário agora é de R${:.2f} reais'.format(s2))
print('teve um aumento de R${:.2f} reais, referente ao antigo'.format(alm))
