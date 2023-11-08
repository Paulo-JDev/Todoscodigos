from datetime import date
info = dict()
info['nome'] = str(input('Nome: ')).strip().title()
info['idade'] = int(input('Ano de nascimento: '))
nasc = info['idade']
info['idade'] = date.today().year - info['idade']
info['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if info['Carteira'] == 0:
    print('-='*20)
    for c, v in info.items():
        print(f'{c} = {v}')
if info['Carteira'] > 0:
    info['Contratação'] = int(input('Ano de contratação: '))  # 35 anos de colaboração
    info['Aposentadoria'] = date.today().year - info['Contratação']
    while True:
        if info['Aposentadoria'] < 35:
            info['Aposentadoria'] += 1
        elif info['Aposentadoria'] > 35:
            info['Aposentadoria'] -= 1
        else:
            break
info['Aposentadoria'] = (info['Contratação'] - nasc) + (info['Aposentadoria'])
info['Salario'] = int(input('Salario: '))
for c, v in info.items():
    print(f'{c} tem o valor {v}')
