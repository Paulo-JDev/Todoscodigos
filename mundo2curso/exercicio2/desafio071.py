print('='*25)
print('{:^25}'.format('BANCO RAIOBR'))
print('='*25, '\nNOTAS DISPONIVEIS: R$100, R$50, R$20, R$10, R$5, R$1')
valor = int(input('Qual valor você quer sacar? '))
total = valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} de R${ced} Reais')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Muito obrigado pela preverência. Volte sempre!!!')
