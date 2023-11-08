dist = float(input('Qual é a distancia da sua viajem:'))
print('Vamos calcular o preço da sua passagem conforme a distancia da viajem')
print('até 200Km cada km custa R$0,50\nacima dessa distancia cada Km fica por R$0,45')
if dist <= 200:
    print('Sua viagem e de {} Km, assim sua passagem ficou por R${} Reais'.format(dist, dist * 0.50))
else:
    print('Sua viagem e de {} Km, assim sua passagem ficou por R${} Reais'.format(dist, dist * 0.45))
