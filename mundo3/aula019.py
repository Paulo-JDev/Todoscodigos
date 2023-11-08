""" Variáveis Compostas (DICIONÁRIOS) """
# dadis = dict()
# dados = {'nome': 'Pedro', 'idade': 25}
# as duas formas de se nomear um dicionario
# print(dados['nome'])
# print(dados['idade'])
# dados['Sexo'] = 'M'
# print(dados)
# del dados['idade']
# print(dados)
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
""" print(filme.values())  # valores. Ex: star wars, 1977 e george lucas
print(filme.keys())  # chaves. Ex: titulo, ano e diretor
print(filme.items())  # itens. Ex: tudo
print('-'*50)
# E tbm podemos usar isso com o FOR
# for k, v in filme.items():
#    print(f'O {k} é {v}')
print(f'O filme {filme["titulo"]} lançou em {filme["ano"]}')
for k in filme:
    print(k)
print('-'*50)
for va in filme.values():
    print(va)
del filme['diretor']
filme['ano'] = 1978
print('-'*50)
filme['Local'] = 'EUA'
for k, va in filme.items():
    print(f'{k} = {va}')
print()
print('-'*40)  # ===========================================
print()
brasil = []
estado1 = {'uf': 'Goias', 'sigla': 'GO'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'DF'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])
print(brasil)"""
estado = dict()
brasil = list()
for c in range(1, 4):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().capitalize()
    estado['Sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy())  # AO INVES DISSO [:] USE ISSO -> .copy()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
    # for k, v in e.items():
    #    print(f'O campo {k} tem valor {v}')

