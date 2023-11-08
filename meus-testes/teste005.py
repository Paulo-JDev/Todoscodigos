import random
print('Escolha cara ou coroa')
meu = str(input('Digite sua escolha:')).strip().lower()
lst = ['coroa', 'cara']
escolha = random.choice(lst)
if meu == escolha:
    print('Vc acertou, caiu {}'.format(escolha))
else:
    print('mais sorte na proxima, oque caiu foi {}'.format(escolha))
