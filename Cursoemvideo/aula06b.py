print('=================Calculadora de Soma==================')
n1 = int(input("Digite um numero:"))
n2 = int(input('diite mais um número:'))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('e sua raiz quadrada é {:.2f}'.format(pow(s, (1/2))))
