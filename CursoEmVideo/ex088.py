print('Avaliador de nota')
le = []
ll = []
x = 's'
loo = 0
while x  in 'SsNn':
    n1 = 0.0
    n2 = 0.0
    le.append(input('Nome: '))
    n1 = float(input('Nota1: '))
    le.append(n1)
    n2 = float(input('Nota2: '))
    le.append(n2)
    rr = (n1 + n2) / 2
    le.append(rr)
    ll.append(le)
    le = []
    #loo = loo + 1
    x = input('Deseja Continuar?[S/N]')
    while x not in 'SsNn':
        x = input('Deseja Continuar?[S/N]')
    if x in 'Nn':
        break
print('-='*20)
print('No. ', end='')
print('NOME                ', end='')
print('MÉDIA')
print('-='*10, end='')
print('=-'*10)
x = 0
while x in range(0 , len(ll)):
    print(f'{x:<3}{ll[x][0]:<20} {ll[x][3]:<20}')
    x = x + 1

x = 1000
while x != 999:
    if x == 999:
        break
    x = int(input('Mostra nostas de qual aluno? (999 para interromper): '))
    while x not in range(0 , len(ll)):
        print(f'Esse valor é invalido informe um o valor entre 0 e {len(ll)}')
        x = int(input('Mostra nostas de qual aluno? (999 para interromper): '))
        #print(f'A nota de {ll[x][0]} são {ll[x][1]} {ll[x][2]} ')
        if x == 999:
            break
    if x != 999:
        print(f'A nota de {ll[x][0]} são [{ll[x][1]}, {ll[x][2]}] ')
    
print('Final do Script')
