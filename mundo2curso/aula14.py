n = 1
impar = par = 0
while n != 0:
    n = int(input("digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de pares foi de {} e de impares foi de {}'.format(par, impar))
