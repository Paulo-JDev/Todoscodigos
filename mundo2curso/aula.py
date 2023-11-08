print('jogo de escolhas')
se = ''
print('vc esta numa estrada, vc escolhe\033[1;36m esquerda\033[m ou \033[1;33mdireita\033[m?')
diresao = str(input('escolha:')).strip().lower()
if diresao == 'esquerda':
    print('Indo pela esquerda vc entrou num armazem e encontrou dois itens, um machado e um mapa')
    esc1 = str(input('so pode escolher um, qual vc escolhe?')).strip().lower()
    if esc1 == 'mapa':
        print('depois de sair do armazem, vc encontrou um posto, viu um carro entrando '
              'nele e usando o mapa para ir para casa')
        print('mais detalhes,na continuação.................')
    elif esc1 == 'machado':
        print('depois de sair do armazem, vc deu de cara com vandalos e usou seu machado '
              ' e roupou o carro deles')
        esc11 = str(input('Vc ta dentro so carro e pode ir para oeste aonde tem sobreviventes \nOU\n'
                          'Ir para o leste aonde pode ter alguma informação de seus amigos')).strip().lower()
        if esc11 in 'Oo':
            print('VC segui para o oeste, com a esperança de encontrar algum dos seus amigos ou '
                  'achar algum que saiba alguma coisa relacionada')
        elif esc11 in 'Ll':
            print('Continua')
        print('mias detalhes na continuação.................')
elif diresao == 'direita':
    print('seguindo pela direita,vc foi capturado e levado.')
    print('VC acorda em um lugar escuro e frio, e dois homens começam a falar com vc\n'
          '\nE te perguntam oque estava fazendo?'
          '\nVC tem duas escolhas vc pode tentar sair(eles estão desarmados) ou tentar entar na jogo'
          'e descobrir oque eles querem')
    esc2 = int(input('Qual vc escolhe a 1 ou a 2?'))
    # if esc2 == 1:
    #    print('VC consegue se desamarrar e pega o carro deles, e acha uma pista interresante'
    #          'sobre aonde pode estar seu colega')
    while esc2 == 1:
        print('Vc ate consegue se desamarar mas eles percebem e como então em maior numero vc acaba morrendo')
        se = str(input('Vc quer continuar: [S/N]'))
        if se in 'Ss':
            esc2 = int(input('escolha de nova:'))
        elif se in 'Nn':
            break
    if esc2 == 2:
        print('Vc conta que estava com fome e estava atraz de comida, então os bandidos acreditam em vc'
              '\nporem eles pedem para vc ajudar em uma certa tarefa e '
              'como recompensa eles iriam dar um pouco de comida')
    print('Continua na proxima parte...........')
print('VC acabou')
