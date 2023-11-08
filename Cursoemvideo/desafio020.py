import random
print('so o nome do lider do grupo')
al1 = str(input('grupo:'))
al2 = str(input('grupo:'))
al3 = str(input('grupo:'))
al4 = str(input('grupo:'))
juntar = [al1, al2, al3, al4]
random.shuffle(juntar)
print('A ordem dos grupos será \n{}'.format(juntar))
