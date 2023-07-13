le = dict()
ll = list()
golpartida = 0
nomejogador = str(input(f'Qual o nome do jogado? '))
x = int(input(f'Digite a quantidade de partidas jogadas pelo o jogador ,{nomejogador}? '))
print('-='*15 + '=-'*15)
i= 0
for i in range(0, x):
    ll.append(int(input(f'Digite a quantidade de gol(s) feitos por {nomejogador}, na {i+1}ª partida? ')))
print('-='*15 + '=-'*15)
le = {"nome": f'{nomejogador}',
    #"partida": f'{x+1}',
    "gol": f'{list(ll)}',
    "total" : f'{sum(ll)}'}
print('-='*15 + '=-'*15)
print(le)
print('-='*15 + '=-'*15)
print(f'O campo nome tem o valor {le["nome"]}.')
print(f'O campo gols tem o valor {le["gol"]}.')
print(f'O campo total tem o valor {le["total"]}.')
print('-='*15 + '=-'*15)
print(f'O jogador {le["nome"]} jogou {x}.')

i = 0
for i in range(0, x):
    print(f'Na partida {i+1} fez {ll[i]}')
    print(f'{le["gol"][i]}')




