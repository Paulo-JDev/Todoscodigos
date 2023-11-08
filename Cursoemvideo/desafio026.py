fra = input('Digite uma frase:').strip().lower()
print('A letra a aparece: {} vezes'.format(fra.count('a')))
print('A primeira vez que aparece é na posição {}'.format(fra.find('a') + 1))
ulti = fra.rfind('a') + 1
print('A ultima vez que a letra a aparece e na posição {}'.format(ulti))
