print('\033[1;33mPare o programa digitando 999\033[m')
print('\033[1;34m-'*20, 'SOMA DE VALORES', '-'*20)
num = int(input('\033[mDigite um valor: '))
# ou num = 0 (tanto faz, no primeiro modo que EU fiz)
cont = soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor: '))
print('Vc digitou {} números e a soma entre todos foi de {}'.format(cont, soma))
