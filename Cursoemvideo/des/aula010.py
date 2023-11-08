tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Seu carro esta novo')
else:
    print('seu carro ja ta mais usado')
print('----fim----')

# ======================================================================

nome = str(input('Qual é o seu nome?')).strip().title()
if nome == 'Paulo':
    print('Que nome mais maneiro')
else:
    print('seu nome é normal')
print('Bom dia, {}'.format(nome))

# ====================================================

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua media foi de {:.2}'.format(m))
if m < 5:
    print('Vc esta de recuperação')
else:
    print('Parabens vc passou')
print('===fim===')
