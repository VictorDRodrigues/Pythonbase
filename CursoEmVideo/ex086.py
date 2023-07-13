le = []
ll = []
x = 0
print('=-' * 20) 
# Le, e coloca a string dentro da lista
while x in range(0,3): #loop de 3 linhas
    le = []
    i = 0
    while i in range(0,3): #loop de 3 colunas
        le.append(int(input(f'Digite um valor para [{x}, {i}]: ')))
        i = i + 1
    ll.append(le)
    x = x + 1
#completou lista de valores,
#resete de valores para correr as linhas
x = 0
print('=-' * 20) 
#mostrando a matriz
while x in range(0,3):
    print(f'[ {ll[x][0]} ][ {ll[x][1]} ][ {ll[x][2]} ]')
    x = x + 1
print('=-' * 20) 
#adicionar variaveis para guarda as informações necessarias
npar = 0
somaterceira = 0
maiordasegunda = 0
#buscando dados
x = 0
i = 0
while x in range(0,3): #loop de 3 linhas
    while i in range(0,3): #loop de 3 colunas
        #print(f'dentro {int(ll[x][i])}')
        if int(ll[x][i]) > 1 and float(int(ll[x][i])% 2) == 0:#verificar seo valor da matriz é par
            npar = npar + ll[x][i]

        if i == 2: # verifica se esta na terceira coluna
            somaterceira = somaterceira + int(ll[x][i])

        if x == 1 and maiordasegunda < int(ll[x][i]):#verificar se esta na 2 linha e se o número é maior que o valor anterior salvo
            maiordasegunda = int(ll[x][i])
        i = i + 1
    x = x + 1
    i = 0
print(f'A soma dos valores pares é {npar}')
print(f'A soma da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {maiordasegunda}')
print('Final do Script...') 
