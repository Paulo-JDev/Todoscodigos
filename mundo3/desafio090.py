escola = {}
escola['Nome'] = str(input('Nome: ')).strip().title()
escola['Média'] = float(input(f'Média do {escola["Nome"]}: '))
if escola['Média'] < 7:
    escola['Situação'] = 'Recuperação'
elif escola['Média'] < 5:
    escola['Situação'] = 'Reprovado'
else:
    escola['Situação'] = 'Aprovado'
print('-='*20)
for k, v in escola.items():
    print(f'{k} é igual a {v}')
