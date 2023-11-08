nome = str(input('Qual seu nome?'))
n = str(input('Qual é o seu sexo: [F/M]?')).upper().strip()
while n != 'M' and n != 'F':
    n = str(input('Dados inválidos. Qual é o seu sexo: [F/M]?')).upper().strip()
print('Sexo {} registrado com sucesso'.format(n))
