while True:
    num = int(input('Quer ver a tabuada de qual numero: '))
    if num <= 0:
        break
    print('-'*20)
    for t in range(1, 11):
        print(f'{num} x {t} = {num * t}')
    print('-'*20)
print('Fim da Tabuada. Volte sempre!')
