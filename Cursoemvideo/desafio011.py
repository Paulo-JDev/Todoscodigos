la = float(input('Qual é a largura da sua parede?'))
al = float(input('Qual é a altura da sua parede?'))
ar = la * al
ti = float(ar / 2)
print('sua parede tem {}m² de área'.format(ar))
print('Sabendo que com um litro de tinta pinta 2m²', end=' ')
print('é a sua tendo {}m²\nVocê ira precisar de {} litros de tinta pra pinta-lá'.format(ar, ti))
