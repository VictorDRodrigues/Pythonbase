import copy
le = []
llista = []
lmaior = []
lmenor = []
r = 0
x = 'S'
validarmaiorpeso = 0
validarmenorpeso = 999999999999999

print('=-' * 20) 
# Le, e coloca a string dentro da lista
while x in 'SsNn':
    if r == 0: # caso seja primera vez implementando dados na lista le
        le.append(str(input('Digite Nome: ')))
        le.append(int(input('Digite Peso: ')))
        r = 1
    else: # altera valor dentro da lista le, para insersção do valor atual do loop
        le[0] = str(input('Digite Nome: '))
        le[1] = int(input('Digite Peso: '))

    #fazer uma copia do valor da lista le para dentro da llista
    llista.append(le[:])
    #validador de resposta para continuar o script
    x = str(input('Quer continuar?[S/N]'))
    while x not in 'SsNn':
        x = str(input('Quer continuar?[S/N]'))
    if x in 'Nn': #caso a resposta seja negativa 'Nn' encerra loop
        break 
#completou lista de valores

print(f'O total de pessoas cadastradas é de {len(llista)}')

#loop da lista, para verificar qual é o maior e menor valor da lista.
print(llista)
r = 0
for r in range(0, len(llista)):
    if int(llista[r][1]) > validarmaiorpeso:
        validarmaiorpeso = int(llista[r][1])
    if int(llista[r][1]) < validarmenorpeso:
        validarmenorpeso = int(llista[r][1])
    r = r + 1

#print(f'validarmaiorpeso = {validarmaiorpeso}')
#print(f'validarmenorpeso = {validarmenorpeso}')

#loop da lista, para adicionar os valores correspondetes ao menor e maior valor.
i = 0
for i in range(0, len(llista)):
    if llista[i][1] == validarmenorpeso:
        lmenor.append(llista[i])

    if llista[i][1] == validarmaiorpeso:
        lmaior.append(llista[i])
    i = i + 1
    
i = 0
print(f'O maior peso dentro da lista informada é de {validarmaiorpeso}Kg.', end='')
for i in range(0, len(lmaior)):
    print(f' [{lmaior[i][0]}]', end=' ')
print('')
print(f'O Menor peso dentro da lista informada é de {validarmenorpeso}Kg.', end='')
i = 0
for i in range(0, len(lmenor)):
    print(f' [{lmenor[i][0]}]', end=' ')
print('')
print('Final do Script...') 
