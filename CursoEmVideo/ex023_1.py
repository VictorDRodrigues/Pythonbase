n = input('Digite um número de 0 a 9999: ')

for posicao, digito in enumerate(n[::-1]):
    print('Unidade de {}: {} ..... {} i'.format(['Unidade', 'Dezena', 'Centena', 'Milhar'][posicao], digito, posicao))
