print('Programa de DESCONTO por FORMA DE PAGAMENTO para um produto!!!')

v = float(input('Informe o VALOR do PRODUTO(exemplo: 999.99): '))

r = int(input('Informe forma de pagamento!!!\n1- À VISTA\n2- À VISTA no CARTÃO\n3- Em até 2x no CARTÃO\n4- 3x ou mais no CARTÂO\n:'))

if r < 1 or r > 4:
    print('Nem uma Opção VALIDA foi escolhida!!!')
elif r == 1:
    v = v*0.9
    print('O VALOR do produto ficou em "R${:.2f}" À VISTA!!!'.format(v))
elif r == 2:
    v = v*0.95
    print('O VALOR do produto ficou em "R${:.2f}" À VISTA no CARTÃO!!!'.format(v))
elif r == 3:
    v = v
    print('O VALOR do produto ficou em "R${:.2f}" em 2x no CARTÃO!!!'.format(v))
elif r == 4:
    v = v*1.2
    print('O VALOR do produto ficou em "R${:.2f}" em 3x ou MAIS no CARTÃO!!!'.format(v))

print('Fim do script.')
