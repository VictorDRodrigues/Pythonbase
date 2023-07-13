print('Desenvolvendo de uma tabela de FIBONACCI!!!)')

r = int(input('Digite o valor INTEIRO do tamanho da sua tabela de BIBONACCI: '))
rt = 0


t = 0
n = 0
na = 0
nc = 1

strin = '0'
stadd = ''

while rt < r:
    t = n
    n = nc + na
    nc = nc + na
    na = t
    stadd = str('{}'.format(n))
    strin = strin + '➝' + stadd
    rt = rt + 1
    #print ('n{} nc{} na{} t{}'.format(n,nc,na, t))

print('O sua tabela de FIBONACI ficou iguala \n"{}"'.format(strin))

print('Fim do Script')
