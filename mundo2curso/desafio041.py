import datetime
print('Categoria de acordo com a idade')
idade = int(input('Qual ano vc nasceu?'))
calc = datetime.date.today().year - idade
print(f'O atleta tem {calc} anos')
if calc <= 9:
    print('Classificação: MIRIM')
elif calc <= 14:
    print('Classsificação: INFANTIL')
elif calc <= 19:
    print('Classificação: JUNIOR')
elif calc <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MESTER')

