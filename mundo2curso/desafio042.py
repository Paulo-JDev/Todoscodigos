print('Se com as retas propostas, pode-se fazer um triangulo')
l1 = float(input('Primeira reta:'))
l2 = float(input('Segunda reta:'))
l3 = float(input('Terceira reta:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('as retas podem formar um triangulo')
    if l1 == l2 == l3:
        print('O triangulo formado é um Equilátero:\n'
              'Todos os lados são iguais')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('O triangulo formado é um Isóceles:\n'
              'dois lados são iguais')
    elif l1 != l2 != l3:
        print('O triangulo formado é um Escaleno:\n'
              'todos os lados são diferentes')
else:
    print('As retas não podem formar um triangulo')
