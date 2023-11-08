print('desconto de 5% em todos os produtos, insira o valor original abaixo e descubra seu novo valor ')
pre = float(input('valor original do produto:R$'))
des = (pre * 5)/100
new = pre - des
print('O desconto foi de R${:.2f} reais'.format(des))
print('O novo valor do produto é R${:.2f} reais'.format(new))
