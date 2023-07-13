print('Progama de analise de números inteiros!!!(Digite 999 para sair)')
n = 0
r = 0
rr = 'S'
nt = 0
na = 0
nz = 99999999999999999999999999999999999999999999999999999999999999999
while rr == 'S':
    r = int(input('Digite valor: '))
    n = n + r
    nt = nt + 1
    rr = input('Desejar continuar adicinando números?(S/N) ').upper()
    if na < r:
        na = r

    if nz > r:
        nz = r

    if rr != 'S':
        rr = 'N'

m = n / nt
print("O valor total da somatoria de todos os números é de: {:.0f}".format(n))
print("O valor da média é de: {:.0f}".format(m))
print("O valor do maior número é de: {:.0f}".format(na))
print("O valor do menor número é de: {:.0f}".format(nz))