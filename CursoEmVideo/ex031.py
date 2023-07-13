print('Vamos calcular o valor da passagem da viagem!')
n = float(input('Digite a distância da sua viagem em Km: '))

if n <=200:
    r = float(n * 0.5)
    print('O valor da sua passagem foi de {}R$'.format(r))
else:
    r = float((n-200) * 0.45 + 100)
    print('O valor da sua passagem foi de {}R$'.format(r))

print('Final do script')
