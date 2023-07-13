print('Desenvolvendo de uma tabela de FIBONACCI!!!)')

r = int(input('Digite o valor INTEIRO do tamanho da sua tabela de BIBONACCI: '))

t = 0
n = 0
na = 0
nc = 1

strin = '0'
stadd = ''

while n <= r:
    t = n
    n = nc + na
    nc = n + na
    na = t
    stadd = str('➝{}'.format(n))
    strin = strin + stadd

print('O sua tabela de FIBONACI ficou iguala \n"{}"'.format(strin))

print('Fim do Script')
