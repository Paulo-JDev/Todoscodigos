import time
num1 = float(input('Primeiro número:'))
num2 = float(input('Segundo número:'))
print('==========MENU===========')
print('\033[1;34m   [1] Somar\n   [2] Mutiplicar\n   [3] Maior\n   [4] Novos números\n   [5] Sair do programa\033[m')
escolha = int(input('\033[1;32m>>>>>>Escolha:\033[m '))
while escolha != 5:
    if escolha == 1:
        print(f'A soma entre {num1} e {num2} = {num1 + num2:.2f}')
        time.sleep(1)
    elif escolha == 2:
        print('{} X {} é igual a {:.2f}'.format(num1, num2, num1 * num2))
        time.sleep(1)
    elif escolha == 3:
        print(f'entre {num1} e {num1} o maior é {max(num1, num2)}')
        time.sleep(1)
    elif escolha == 4:
        print('------------------------------')
        num1 = float(input('Digite outro valor: '))
        num2 = float(input('Digite outro valor: '))
    else:
        print('Opção inválida. tente novamente')
        time.sleep(1)
    print('==========MENU===========')
    print('\033[1;34m   [1] Somar\n   [2] Mutiplicar\n   '
          '[3] Maior\n   [4] Novos números\n   [5] Sair do programa\033[m')
    escolha = int(input('\033[1;32m>>>>>>Escolha:\033[m '))
print('\033[1;31mVC SAIU DO PROGRAMA\033[m, volte sempre')
