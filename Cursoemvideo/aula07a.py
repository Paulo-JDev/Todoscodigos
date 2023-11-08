n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
print('A soma foi {}\no produto foi {}\na divisão foi {:.2f}'.format(s, m, d, di), end=' ')
print('A divição inteira foi {} e a potencia {}'.format(di,(n1 ** n2)))
