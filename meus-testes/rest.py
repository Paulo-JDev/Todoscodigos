import random
Objetivo1 = 'Parar os habitantes monstruosos da masmorra de atacar o mundo da superfície.'
Objetivo2 = 'Frustrar a trama de um vilão maligno.'
Objetivo3 = 'Destruir uma ameaça mágica dentro de uma masmorra.'
ListaObjetivo = [Objetivo1, Objetivo2, Objetivo3]
ObjetivoAtual = random.choice(ListaObjetivo)
print('O Objetivo da missão é {}'.format(ObjetivoAtual))
