import datetime
print('-' * 40)
print('tudo que eu aprendir no curso')
print('-' * 40)
nome = str(input('Qual é o seu nome?')).title().strip()
idade = int(input('quantos anos vc tem?'))
hobby = str(input('Qual seu hobby favorito?')).strip().lower()
mora = str(input('Aonde vc mora?')).strip()
t = {'lim': '\033[m',
     'ver': '\033[4;32m'}

# ================================= NOME ==================================

print('-' * 20)
junta = nome.split()
curios = ''.join(junta)
if junta[0] == 'Paulo':
    print('Que nome massa')
elif nome in 'Fernando Matheus Maria Juliane Juan':
    print('que nome interresante vc tem')
print('Prazem em te conhecer\033[1;33m {}\033[m \n'
      'se vc fosse pro exercito seu nome lá dentro seria \033[4;31m{}\033[m'.
      format(junta[0], junta[len(junta) - 1]))
print('\033[4;35mCuriosidade inultil\033[m, sabia que seu nome tem \033[1;36m{} letras\033[m'.format(len(curios)))

# ================================= IDADE ==================================

print('-' * 20)
if idade + 1 == 18:
    print('Ja ta perto de fazer 18 anos')
elif idade > 18:
    print('Vc ja é de maior')
elif idade == 18:
    print('Agora que vc e de maior ta pensando em que?')
else:
    print('Época boa quando vc é de menor idade')
ano = datetime.date.today().year - idade
print('e vc nasceu em {}{}{}'.format(t['ver'], ano, t['lim']))

# ================================= HOBBY =================================

print('-' * 20)
if hobby == 'jogar videogame':
    print('\033[1;34;40mQue hobby maneiro\033[m')
elif hobby == 'estudar' or hobby == 'limpar a casa':
    print('\033[1;34;40mVc é responsalvel até demais\033[m')
elif 'assistir tiktok' == hobby or hobby == 'fumar':
    print('\033[1;34;40mQue bosta em, que tal capinar um lote ou ajudar alguém\033[m ')
else:
    print('\033[1;34;40mQue hobby interresante, vc tem \033[m')
print('-' * 20)
