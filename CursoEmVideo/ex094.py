le = dict()
ll = list()
lm = list()
x = 's'
while x in 'SsNn':
    nm = str(input('Nome:'))
    sx = str(input('Sexo: [M/F]'))
    ag = int(input('Idade:'))
    le = {
        'nome': f'{nm}',
        'sexo': f'{sx.upper()}',
        'idade': f'{ag}'
        }
    ll.append(le)
    if sx == 'F':
        lm.append(le)
    
    x = str(input('deseja continuar a adicionar? [S/N] '))
    while x not in 'SsNn':
        x = str(input('deseja continuar a adicionar? [S/N] '))
    if x in 'Nn':
        break
print('-='*15 + '=-'*15)
print(f'A quantidade de pessoas cadastradas é {len(ll)}')
print('-='*15 + '=-'*15)
somaidade = 0
i = 0
while i in range(0, len(ll)):
    somaidade = somaidade + int(ll[i]['idade'])
    i = i + 1
media = somaidade/len(ll)
print(f'A média de idade do grupo cadastrado é de {media}')
print('-='*15 + '=-'*15)
print(f'A lista com todas as mulheres ')
p = 0
for p in range(0, int(len(lm))):
    print(lm[p])
    p = p + 1
print('-='*15 + '=-'*15)
print('A lista com todos os valores com idade a cima da idade média ')
i = 0
while i in range(0, len(ll)):
    if media <= int(ll[i]['idade']):
        print(f'{ll[i]}')
    i = i + 1
print('-='*15 + '=-'*15)
print('-='*15 + '=-'*15)
print('-='*15 + '=-'*15)
#print(ll)
print('Final do Script...')
    
