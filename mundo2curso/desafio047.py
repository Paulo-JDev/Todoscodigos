for p in range(2, 51, 2):
    print(p, end=' ')
print('fim1')

# ===========================================

for p in range(2, 51):
    if p % 2 == 0:
        print(p, end=' ')
print('fim2')

# ==============================================
print('\nI Com While I\n')

num = 0
while num <= 50:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1
print('fim3')

# ==============================================

n = 0
while True:
    if n % 2 == 0:
        print(f'{n}', end=' ')
    n += 1
    if n == 51:
        break
print('fim4')
