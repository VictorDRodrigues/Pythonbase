r = int(input('Informe um número inteiro qualquer para ter a sua tabuada até o 10ª termo: '))

print('A tabuado de de {} é'.format(r))

for i in range(1,11):
    print(' {} x {} = {}'.format(i,r,r*i))
