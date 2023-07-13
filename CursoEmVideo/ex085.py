import copy
le = []
llista = []
lpar = []
limpar = []
x = 0
i = 0
print('=-' * 20) 
# Le, e coloca a string dentro da lista
while x in range(0,7):
    le.append(int(input(f'Digite o {x+1}ª Valor: ')))
    x = x + 1
#completou lista de valores
#fazer uma copia do valor da lista le para dentro da llista
i = 0
for i in range(0, len(le)):
    if float(le[i]) % 2 == 0:
        lpar.append(le[i])
    if float(le[i]) % 2 > 0:
        limpar.append(le[i])
    i = i + 1

print(f'Os valores pares difitados foram: {lpar}',)
#print(lpar)
print(f'Os valores impares difitados foram: {limpar}',)
#print(limpar)
#print('')

r = 0
'''
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

'''
print('Final do Script...') 
