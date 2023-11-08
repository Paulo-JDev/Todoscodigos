f1 = input('Digite algo:')
print('O tipo primitivo desse valor é', type(f1))  # A primeira parte do f1.is---- é a variavel(objeto)
print('E um número?{}'.format(f1.isnumeric()))   # isnumeric=numero é quando so tem numero
print('É alfabético?{}'.format(f1.isalpha()))  # isalpha=alfabetico quando so tem letra
print('Só tem espaços?{}'.format(f1.isspace()))  # isspace=espaços quando so tem espaços
print('Esta em ciaxa-alta?{}'.format(f1.isupper()))  # isupper=maiúsculas é quamdo so tem maiúculas
print('Esta em minusculas?{}'.format(f1.islower()))  # islower=minusculas é quando so tem minusculas
print('Esta alfanumerico?{}'.format(f1.isalnum()))  # islnum=alfanumerico [e quando tem um numero é uma letra juntos
print('Esta capitalizada?{}'.format(f1.istitle()))
# istitle=capitalizada é Paulo, quer dizar que tem partes em up e outras em lower
