import math
nu1 = float(input('Digite o cateto adjacente:'))
nu2 = float(input('Digite o cateto oposto:'))
hip = (nu1**2)+(nu2**2)
print('A hipotenussa do triangulo é {:.2f}'.format(pow(hip, (1/2))))

from math import hypot
co = float(input('O valor do cateto oposto:'))
ca = float(input('o valor do cateto adjacente:'))
hi = hypot(ca, co)
print('A hipotenusa do triangulo em guestão é {}'.format(hi))
