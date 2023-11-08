palavras = ('gratis', 'estudar', 'mercado', 'depois', 'vamos', 'amarelo', 'azul', 'video', 'livros', 'matematica')
print('='*50)
print(f'{"VOGAIS":^50}')
print('='*50)
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('')
print('='*50)
