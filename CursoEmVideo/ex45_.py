import random

print('Jogo de Jokenpô')

# Constantes para as jogadas
PAPEL = 1
PEDRA = 2
TESOURA = 3

# Dicionário com as combinações possíveis e seus resultados
combinacoes = {
    (PAPEL, PEDRA): 'Ganhou',
    (PEDRA, TESOURA): 'Ganhou',
    (TESOURA, PAPEL): 'Ganhou',
}

# Geração da jogada da máquina
maquina = random.randint(1, 3)

print('Regra do Jokenpô\nPedra ganha Tesoura\nPapel ganha Pedra\nTesoura ganha Papel')

# Entrada do jogador
jogador = int(input('Entre:\n1 - Papel\n2 - Pedra\n3 - Tesoura\n'))

print('Você {} x {} Máquina'.format(jogador, maquina))

# Verificação do resultado
if jogador == maquina:
    print('Empate')
else:
    resultado = combinacoes.get((jogador, maquina))
    if resultado:
        print(resultado)
    else:
        print('Perdeu')
