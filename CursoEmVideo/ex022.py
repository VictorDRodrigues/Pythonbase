n = input('Escreve um nome:')

print('MAIUSCULO : {}'.format(n.upper()))

print('minusculo : {}'.format(n.lower()))

print('O nome tem o total de letras de : {}'.format(len(n) - n.count(' ') ))

print('O seu primeiro nome tem {}'.format(n.find(' ')))