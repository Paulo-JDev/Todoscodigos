# referente a aula 9
""" programa que lê o nome de alguem e faz algumas mudanças"""
nome = str(input('Digite o seu nome:')).strip()

print('Seu nome inteiro em maiúsculos: {}'.format(nome.upper()))
print('O nome com as primeiras letra em maiúculas: {}'.format(nome.title()))
print('Seu nome inteiro em minúsculas: {}'.format(nome.lower()))

total = nome.split()
print('Total de letras no nome: {}'.format(len(''.join(total))))
print('{}'.format(len(nome) - nome.count(' ')))

pri = nome.split()
conta = pri[0]
lm = len(conta)
print('tem: {} letras'.format(lm))
