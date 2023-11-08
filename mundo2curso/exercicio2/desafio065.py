resp = 'Ss'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Vc digitou {} números e a media entre eles é de {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

lista = []
p1 = 'S'
while p1 in 'Ss':
    num = int(input('Digite um numero : '))
    p1 = input('Quer continuar ? [S/N]').strip().upper()
    lista.append(num)
    if p1 == 'N':
        break
print(f'Você digitou {len(lista)}numeros e a media foi {sum(lista) / len(lista)} \n O maior valor foi {max(lista)} e o menor foi {min(lista)}')


