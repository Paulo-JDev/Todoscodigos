lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# Tuplas são IMÚTAVEIS
# erro: lanche[1] = 'Refrigerante'

for c in lanche:
    print(f'Eu vou comer {c}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('\ncomi muito')

# for cont in range(0, len(lanche)):
#   print(lanche[c], f'na posição {cont}')

# print(sorted(lanche)) # ordena em ordem alfabetica
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print('sorted =', sorted(c))
print('len =', len(c))
print('count =', c.count(5))
print('index =', c.index(8))  # em qual posição ele ta. exe: o 8 ta na 4 posição
# se tever mais de um na tuplas c.index(8, 2) seria a partir da casa 2

pessoa = ('Paulo', 18, 'M', 61.00)
# del = apaga da memoria TODA a tupla
print(pessoa)
