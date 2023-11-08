somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
mulher20 = 0
nomemenos20F = ' '
for p in range(1, 5):
    print('======== {} PESSOA ========'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    if sexo in 'Ff' and idade < 20:
        nomemenos20F += nome
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama de {}'.format(maioridadehomem, nomevelho))
if mulher20 == 1:
    print('Tem somente uma mulher com menos de 20 anos')
else:
    print('Tem {} mulheres menores de 20 anos'.format(mulher20))
