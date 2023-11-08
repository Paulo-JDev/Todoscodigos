import datetime
print('Alistamento')
ano = float(input('Ano em que vc nasceu?'))
ali = datetime.date.today().year - ano
print('vc tem {} anos'.format(ali))
if ali < 18:
    print('Vc ainda vai se alistar\n'
          'ainda falta {} anos'.format(18-(datetime.date.today().year - ano)))
elif ali == 18:
    print('Ja ta na hora de se alistar')
else:
    print('Se vc não se alistou, ja passou o tempo\n ja se passou {} anos'.format(ali - 18))
