mais18 = man = mulher20 = cont = som = som1 = 0
while True:
    print('-'*24)
    print('  CADASTRE UMA PESSOA')
    print('-'*24)
    ida = int(input('Idade: '))
    sex = conti = ' '
    while sex not in 'MmFf':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('='*24)
    if sex in 'Mm':
        man += 1
    if ida >= 18:
        cont += 1
    if sex in 'Ff' and ida < 20:
        mulher20 += 1
    if ida != 0:
        som += ida
        som1 += 1
    while conti not in 'SsNn':
        conti = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if conti in 'Nn':
        break
print('======= FIM DO PROGRAMA =======')
print(f'Ao Todo temos {man} Homens cadastrados')
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'A media entre todos são de {som / som1} anos')
print('E temos {} mulher com menos de 20 anos'.format(mulher20))
