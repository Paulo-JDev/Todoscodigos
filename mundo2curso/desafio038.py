print(20*'-', 'Qual é o maior valor', '-'*20)
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
if n1 > n2:
    print('O primeiro valor é o maior')
elif n2 > n1:
    print('O segundo valor é o maior')
elif n1 == n2:
    print('Não tem valor maior, os dois são iguais')
