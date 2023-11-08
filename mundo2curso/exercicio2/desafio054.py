import datetime
m = 0
n = 0
for c in range(1, 8):
    ano = int(input('Em qual ano vc nasceu?'))
    calc = datetime.date.today().year - ano
    if calc >= 21:
        m += 1
    else:
        n += 1
print('Das 6 pessoas, {} são maiores de idade e {} são menores'.format(m, n))
