print('10 Termos de uma PA')
pri = int(input('Digite o primeiro termo(numero):'))
r = int(input('Razão da PA ou sequência da PA:'))
décimo = pri + (10 - 1) * r
for pa in range(pri, décimo + r, r):
    print('{}'.format(pa), end=' > ')
print('FIM')
