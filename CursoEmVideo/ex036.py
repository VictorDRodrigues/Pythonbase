print('Programa de avaliação de Financiamento de IMOVEL!!!')
vc = float(input('Digite o valor da casa: '))
s = float(input('Digite o valor do salário: '))
t = int(input('Digite a quantidade de anos para pagar: '))
tt = t*12
st = (s*tt)*0.3
pa = vc/tt

print ('Valor total acumalo sobre parcelas ao final do de {} anos, foi de R${}'.format(t,st))

if st >= vc:
    print('Seu Financiamento foi APROVADO!!!')
    print('O valor mínimo da Parcela do Financiamento é de R${:.2f}'.format(pa))
else:
    print('Seu Financiamento foi NEGADO!!!')
    print('O valor mínimo da Parcela do financiamento para o valor informado é de R${:.2f}'.format(pa))

