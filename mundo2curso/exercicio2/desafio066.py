cont = soma = 0
while True:
    num = int(input('Digite um numero (999 faz parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi de {soma}')
