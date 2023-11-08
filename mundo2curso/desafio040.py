print(20*'-', '\033[4;34mMedia de um aluno\033[m', '-'*20)
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Você está\033[1;31m reprovado\033[m')
    print('Com a media: {}'.format(media))
elif media >= 7.0:
    print('Você está \033[1;32maprovado\033[m')
    print('Com a media: {}'.format(media))
else:
    print('Você está de \033[1;33mrecuperação\033[m')
    print('Com a media: {}'.format(media))
