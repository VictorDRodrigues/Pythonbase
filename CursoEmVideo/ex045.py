import random
print('Jogo de Jokenpô')
m = random.randint(1, 3)
print('======================')
print('Regra do Jokenpô\n======================\nPedra   ganha Tesoura\nPapel   ganha Pedra\nTesoura ganha Papel')
print('======================')
r = int(input('Entre:\n1 - Papel\n2 - Pedra\n3 - tesoura\n'))

print('Você {} x {} MAQUINA'.format(r, m))

if r == m:
    print('Deu em Empate')
elif r == 1 and m == 2:
    print('Você Ganhou')
elif r == 2 and m == 3:
    print('Você Ganhou')
elif r == 3 and m == 1:
    print('Você Ganhou')
else:
    print('Perdeu')
print('======================')


