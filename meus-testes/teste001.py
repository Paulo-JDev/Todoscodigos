""" Feitos pelo chatgpt """
pesos = []
for p in range(6):
    peso = float(input('Digite o peso da pessoa {}:'.format(p+1)))
    pesos.append(peso)
pesado = max(pesos)
leve = min(pesos)
print('O mais pesado pesa:', pesado)
print('O mais leve pesa: {}'.format(leve))
