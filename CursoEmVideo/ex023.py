n = input('Digite 1 número de 0 a 9999 : ')

nn = int(n)
t = int(len(n))

if t == 4:
    print('Unidade de Milhar : {}'.format(n[0]))
    print('Unidade de Centena : {}'.format(n[1]))
    print('Unidade de dezena : {}'.format(n[2]))
    print('O valor de Unidade é de : {}'.format(n[3]))

elif t == 3:
    print('Unidade de Centena : {}'.format(n[0]))
    print('Unidade de dezena : {}'.format(n[1]))
    print('O vvalor de Unidade é de : {}'.format(n[2]))

elif t == 2:
    print('Unidade de dezena : {}'.format(n[0]))
    print('O valor de Unidade é de : {}'.format(n[1]))
else:
    print('O valor de Unidade é de : {}'.format(n[0]))