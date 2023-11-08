import random
nu1 = str(input('Primeiro aluno: '))
nu2 = str(input('Segundo aluno: '))
nu3 = str(input('terceiro aluno: '))
nu4 = str(input('Quarto aluno:'))
lst = [nu1, nu2, nu3, nu4]
escolhido = random.choice(lst)
print("o aluno escolhido foi: {}".format(escolhido))
