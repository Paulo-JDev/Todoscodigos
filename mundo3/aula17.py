mate = ['lapis', 'papel', 'caneta', 'borracha']
print(mate)
mate[2] = 'caderno'
print(mate)
# LISTA SÃO MUTAVEIS
mate.append('regua')
print(mate)
tst = mate.append(str(input('Digite um material: ')).strip().lower())
print(mate)
mate.insert(1, 'ferro')
for m in mate:
    print(m, end=' ')
del mate[1]
print('\n',mate)
# mate.pop(2) remove o local especifico mas e mais usando para apagar o ultimo
#  mate.remove('lapis') remove o item especifico, somente o primeiro se houver mais de um
mate.pop()
print(mate)
print(len(mate), 'Valores no total da lista')
print('\n')

# ==================================================================================

valores = list(range(3, 11))
# da pra reutilizar tudo com o list
print(valores, 'list(range))')
if 3 in valores:
    valores.remove(3)
else:
    print('Não achei o numero 3')
print(valores, 'remove')
va = [8, 2, 5, 4, 9, 3, 0, 2]
for v in va:
    print(v, end=' ')
print()
va.remove(2)
print(va, 'testando o remove')
va.sort()  # organiza em ordem
print(va, 'Novo em ordem crecenste')
va.sort(reverse=True)
# usando .sort(reverse=False) fica em ordem crescende
print(va, 'Ordem decresente')
for c, val in enumerate(va):
    print(f'Na posição {c} achei o número {val}!')
num = list()
for cont in range(0, 5):
    num.append(int(input('Digite um valor:')))
print(num)
a = [1, 2, 3, 4]
# b = a <- isso se torna uma ligação aonde vc muda um e o outro támbem
b = a[:]  # OU a.copy()
b[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')
