togasto = mais1 = vabarato = cont = 0
nomebarato = ' '
print('-'*32)
print('     LOJA SUPER ECONOMICO')
print('-'*32)
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    valor = float(input('Preço: R$'))
    togasto += valor
    cont += 1
    conti = ' '
    if valor > 1000:
        mais1 += 1
    if cont == 1:
        vabarato = valor
        nomebarato = nome
    elif valor < vabarato:
        vabarato = valor
        nomebarato = nome
    while conti not in 'SsnN':
        conti = str(input('VC quer continuar [S/N]: ')).strip().upper()[0]
    if conti in 'Nn':
        break
print('------------- FIM DO PROGRAMA --------------')
print(f'O Volor final dos produtos foi de R${togasto}')
print(f'Tem {mais1} produtos com o valor acima de R$1000')
print(f'O produto mais barato é o {nomebarato} e ele custa R${vabarato}')
