import time
import random
print('Avaliador de vencedor no jogo do DADO')
le = dict()
ll = list()
x = 0
for x in range (0, 4): # são 4 jogadores 1 lance para cada jogador
    dadole = random.randint(1,6) # resultado do lançamento do dado
    le = dict()
    le['jogador'] = str('{}'.format(x+1))
    le['resultado'] = str('{}'.format(dadole))
    ll.append(le.copy())
print('-='*10 + 'Lancaçamento', end='')
print('=-'*10)
x = 0
for x in range (0, len(ll)):
    print(f'O jogador{ll[x]["jogador"]} tirou {ll[x]["resultado"]}')
    time.sleep(0.5)
print('-='*10 + '   Ranking  ', end='')
#ll = sorted(ll, key=lambda y: y['resultado'], reverse= True)
# criei um nova lista para o ranking final da partida
lr = sorted(ll, key=lambda y: y['resultado'], reverse= True) 
print('=-'*10)
for i in range (0, len(lr)):
    print(f'{i+1}ª lugar: jogador{lr[i]["jogador"]} tirou {lr[i]["resultado"]}')
    time.sleep(0.5)
    
print('Final do Script')
