expr = str(input('Dugite uma expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        print(pilha, '1')
        print(len(pilha), '1.2')
        pilha.append('(')
        print(pilha, '2')
        print(len(pilha), '2.2')
    elif simb == ')':
        if len(pilha) > 0:
            print(pilha, '3')
            pilha.pop()
            print(pilha, '3.2')
            print(len(pilha), '3.3')
        else:
            print(pilha, '4')
            pilha.append(')')
            print(pilha, '4.2')
            break
print(pilha)
print(len(pilha))
if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão está errada!')
