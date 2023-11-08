V1 = int(input('Digite a velocidade de um carro:'))
if V1 > 80:
    print('Vc esta multado, por exceder o limite da via')
    multa = (V1 - 80) * 7
    print('Você exedeu {}Km/h e tem que pagar R${:.2f}'.format(V1-80, multa))
else:
    print('Você esta tudo ok, dirija com segurança')
