import random

cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\33[33m',
    'ciano':'\33[36m',
    'pretobranco':'\33[7;30m'}

print('\033[7:33:44mteste\033[m')

rr = random.randint(0,5)
n = int(input('Adivinhe o Número entre {}{}{} e {}{}{}: '.format(cores['amarelo'],0,cores['limpa'],cores['ciano'],5,cores['limpa'])))

if rr == n:
    print('Você ACERTOU!!! O númore é {}'.format(rr))
else:
    print('Você ERROU!!! O númore correto é {}'.format(rr))

print('Fim de script!')
