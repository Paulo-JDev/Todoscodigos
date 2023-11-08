dias = int(input('Quantos dias ficou alugado?'))
km = float(input("Quantos Kms rodados?"))
v1 = dias * 60
v2 = km * 0.15
vt = v2 + v1
print('O total a pagar é de R${:.2f}'.format(vt))
