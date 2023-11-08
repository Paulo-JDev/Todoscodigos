print('Produtos, formas de pagamento')
valor = float(input('Valor do produto:'))
print('a vista dinheiro/chegue: 10% de desconto(opção 1)\n'
      'a vista no cartão: 5% de desconto(opção 2)\n'
      'em ate 2x no cartão: preço normal(opção 3)\n'
      '3x ou mais no cartão: 20% de juros(opção 4)\n')
paga = int(input('Forma de pagamento(opção):'))
if 1 == paga:
    print('O produto ficara {} reais'.format(valor - (valor * 10 / 100)))
    print('Desconto de {}'.format(valor * 10 / 100))
elif 2 == paga:
    print('O produto ficara {} reais'.format(valor - (valor * 5 / 100)))
    print('Desconto de {}'.format(valor * 5 / 100))
elif 3 == paga:
    print('O valor do produto não tera nenhuma alteração')
    print('Cada parcela ficara {} reais'.format(valor / 2))
elif 4 == paga:
    div = int(input('Quantas vezes vc quer dividir:'))
    juros = valor + (valor * 20 / 100)
    print('O produto final ficara em {} reais(com um aumento de 20%)'.format(juros))
    print('cada parcela ficara em {}'.format(juros / div))
else:
    print('Não existe essa forma de pagamento')
