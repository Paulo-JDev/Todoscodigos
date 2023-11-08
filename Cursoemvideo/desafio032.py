print('descobrir se o ano é bissexto(2000 pra frente)')
ano = int(input('Digite o ano:'))
biss = ano % 4
if biss == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
