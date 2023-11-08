i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('acabou')

# ---------------------------------------------------------------------------

print('Tabuada')
num = int(input('Digite um numero:'))
for num in range(0, 10+1, num):
    print(num)

# -----------------------------------------------------------------------------

soma = 0
for d in range(0, 3):
    nume = int(input('Digite um valor: '))
    soma = nume + soma  # ou tbm {soma += nume}
print("A soma de todos os valores foi {}".format(soma))
