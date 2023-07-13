le = []
x = 'S'
while x in 'SsNn':
    i = int(input('Digite um valor: '))
    if i in le:
        print('Valor já existente na lista... Valores não seram duplicados!')
    else:
        le.append(i)
        print('Valor adicionado a lista com sucesso...')

    x = input('Quer continuar?[S/N]')
    while x not in 'SsNn':
        x = input('Quer continuar?[S/N]')
    if x == 'N' or x =='n':
        break
print('Fim de adicão de valores para lista...')
le.sort()
print(le)
    
