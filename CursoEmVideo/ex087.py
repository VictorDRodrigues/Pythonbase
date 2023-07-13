import random
import time
j = 'JOGA NA MEGA SENA'
print('=-' * 26)
print(f'{j:^54}') 
print('=-' * 26) 
le = [] # list de inserção
ll = [] # lista
listacomposta = []
x = 0 # quantidade de jogos
loo = 0 #quantidade de loop
rp = 0

# Le, e coloca a string dentro da lista
loo = int(input('Quantos jogos você quer que eu sorteie? '))
while x in range(0, loo): #loop de jogos
    i = 0 # zera curso de do loop da lista de 1 jogo
    
    while i in range(0,6): # loop de 1 jogo
        le = []
        le.append(random.randint(1, 60))
        if le in ll:
            rp = rp + 1
            le.pop()
            le.append(random.randint(1, 60))
            print(f'Quantidade de items repetidos {rp}')
            i = i - 1
        else:
            ll.append(le)
        le = []
        i = i + 1
        # finzaliza 1 loop dentro do jogo
    listacomposta.append(ll)
    ll = []
    x = x + 1
    # finzaliza 1 loop completo de 6 números
#print(f'll = {listacomposta[0]}')

jj = str(f' SORTEANDO {loo} JOGOS ')
print('-=-=-=', end='')
print(f'{jj:^40}', end='')
print('=-=-=-')
delay = 5
x = 0
while x in range (0, loo):
    listacomposta[x].sort()
    '''
    va1 = listacomposta[x][0]
    va2 = listacomposta[x][1]
    va3 = listacomposta[x][2]
    va4 = listacomposta[x][3]
    va5 = listacomposta[x][4]
    va6 = listacomposta[x][5]'''
    print(f'Jogo Nª{x+1} : {listacomposta[x][0]}, {listacomposta[x][1]}, {listacomposta[x][2]}, {listacomposta[x][3]}, {listacomposta[x][4]}, {listacomposta[x][5]}')
    #print(f'Jogo Nª{x+1} : [{va1}, {va2}, {va3}, {va4}, {va5}, {va6}]')
    x = x + 1
    #time.sleep(0.3)
#print(f'listacomposta = {listacomposta}')
jf = str(f' < BOA SORTE! > ')
print('-=-=-=', end='')
print(f'{jf:^40}', end='')
print('=-=-=-')
print(f'Quantidade de items repetidos {rp}')
print('Final do Script...') 
