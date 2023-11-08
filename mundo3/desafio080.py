val = []
for v in range(0, 5):
    n = int(input('Digite um valor'))
    if v == 0 or n > val[-1]:
        val.append(n)
    else:
        pos = 0
        while pos < len(val):
            if n <= val[pos]:
                val.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem: {val}')
