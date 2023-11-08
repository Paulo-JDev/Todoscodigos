print('=' * 30)
print('ração dos segmentos para formar um triangulo,')
print('digite o valor de cada reta, e descubra se da pra fazer um triangulo ou não')
print('=' * 30)
l1 = float(input('Primeira reta:'))
l2 = float(input('Segunda reta:'))
l3 = float(input('Terceira reta:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um triangulo')
