somaidade = 0
mediaidade = 0
somasalario = 0
mediasalario = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
nomemenos20F = ''
espaco = ' '
for p in range(1, 5):
    print('======== {} PESSOA ========'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    salario = float(input('Sua renda(mensal):'))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    somaidade = somaidade + idade
    somasalario += salario
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    if sexo in 'Ff' and idade < 20:
        nomemenos20F = nomemenos20F + nome + espaco
mediaidade = somaidade / 4
mediasalario = somasalario / 4
print('A media salarial do grupo é de {}Reais'.format(mediasalario))
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama de {}'.format(maioridadehomem, nomevelho))
if mulher20 == 1:
    print('So {}que tem menos de 20 anos entres as mulheres'.format(nomemenos20F))
else:
    print('Tem {} mulheres menores de 20 anos, que são {}'.format(mulher20, nomemenos20F))
