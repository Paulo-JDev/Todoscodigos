from random import randint
from time import sleep
c = 1
print('=='*20)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('=='*20)
total = []
dados = []
jogos = int(input('Quantos jogos você quer que eu sortei? '))
print(f'=-=-=-=-=- SORTEANDO {jogos} JOGOS =-=-=-=-=')
while c <= jogos:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in dados:
            dados.append(n)
            cont += 1
        if cont >= 6:
            break
    dados.sort()
    total.append(dados[:])
    dados.clear()
    c += 1
for p, j in enumerate(total):
    j.sort()
    print(f'Jogo {p+1}: {j}')
    sleep(0.5)
print('=-=-=-=-=-=- Boa Sorte! -=-=-=-=-=-=')
