print('|==========================nota final e média final============================|')
n1 = float(input('Sua nota do primeiro bimestre:'))
n2 = float(input('Sua nota do segundo bimestre:'))
n3 = float(input('Sua nota do Terceiro bimestre:'))
n4 = float(input('Sua nota do quarto bimestre:'))
nf = n1+n2+n3+n4
mf = (n1+n2+n3+n4)/4
print('A nota final foi de {:.2f}\nSua média final foi de {:.2f}'.format(nf, mf))
