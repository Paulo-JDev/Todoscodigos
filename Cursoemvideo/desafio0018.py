import math
ang = int(input('Digete o angulo que vc quer:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno é: {:.2f}\nO cosseno é: {:.2f}\nE a tangente é :{:.2f}'.format(sen, cos, tang))
