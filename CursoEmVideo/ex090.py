print('Avaliador de nota IZ, com dicionario e lista')
le = {}
ll = []
nomei = input('Nome: ')
mediai = float(input('Média: '))
if mediai >= 6:
    r = 'Aprovado'
else:
    r = 'Reprovado'
le = {
    "Nome" : f'{nomei}',
    "Media" : f'{mediai}',
    "Resultado" : f'{r}'
    }

print(f'le que é um dicionario {le}')

ll.append(le.copy())

print(f'll que é uma lista {ll}')
    
print('Final do Script')
