lista = ('Pão', 0.80, 'Leite', 5.00, 'Queijo', 4.00, 'coxinha', 3.00,
         'frango', 15.00, 'Picanha', 28.00, 'halls', 1.50, 'ovos', 15.00,
         'lapis', 1.00, 'borracha', 1.50, 'detergente', 2.59)
print('='*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('='*30)
# COM ENUMERATE:
# for pos, l in enumerate(lista):
#   if pos % 2 == 0:
#       print(f'{l}', end='')
#   else:
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    elif pos % 2 == 1:
        print(f'R$ {lista[pos]:>4}')
print('='*30)
