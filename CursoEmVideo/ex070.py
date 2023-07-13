print('!!!ATACADINHO!!!')
t = p1000 = 0
pb = 99999999999999999
pbs = ''
while True:
    n = str(input('Digite o NOME do Produto: ')).upper()
    p = float(input('Digite o PREÇO do Produto: RS'))
    t = t + p
    if p > 1000:
        p1000 = p1000 + 1
    if pb > p:
        pb = p
        pbs = n
    r = ' '
    while r not in 'SsNn':
        r = str(input('Digite adicionar mais um produto(S/N): ')).strip().upper()
    if r == 'Nn':
        break

print('Total da Compra é de  "R${:.2f}"'.format(t))
print('Total de Produtos com valor maior que R$1000,00 é "{}"'.format(p1000))
print('O nome do produto mais barato é "{}"'.format(pbs))
print('Fim do Script')