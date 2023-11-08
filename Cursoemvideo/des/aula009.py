frase = 'meu exemplo pra aula'
out = 'minecraft é o melhor jogo de mundo aberto e miranha do ps4 fica em 2 e gta em 3'
out2 = 'Mais exemplos pra ficar mais facil de EXEMPLIFICAR na aula '
""" o python começa a contar pelo 0 """

# fatiamento

print(frase)
print(frase[4])
print(out[4:17])
print(frase[4:14:2])

# análise

print(len(frase))    # O len CONTA quantos caracteres tem a frase
print(len(out2))
print(frase.count('e'))
print(frase.count('m', 0, 6))  # funçao cont com o fatiamento
print(out2.find('aula'))  # mostra aonde começa a 'frase'
print(frase.find('Python'))
print('meu' in frase)
print('seu' in frase)

# trasformação

print(out.replace('minecraft', 'Terraria'))
print(out2.replace('na aula', 'no curso'))
print(frase.upper())
print(out2.lower())
print(frase.capitalize())
print(frase.title())
print(out.strip())  # retira os espaços inuteis da frase
out2.rstrip()  # retira os espaços inuteis da frase começando pela direita (r) rigth = direita
out2.lstrip()  # retira os espaços inuteis da frase começando pela esquerda (l) left = esquerda

# Divisão

frase.split()  # cada palavra ganha nova numeração ex:'meu lar' no normal o total teria 6
# agora o meu começa normal mais quando chega no lar recomeça a conta, separando a frase em caixas por palavra,
# exemplo teria 2 caixas
"""estudar melhor a função split"""

burro = frase.split()
print('-'.join(burro))
print(''.join(burro))
print(len(''.join(burro)))
tes = out.split()
print(tes[0])
print(tes[0][4])

# junção

print(','.join(frase))
