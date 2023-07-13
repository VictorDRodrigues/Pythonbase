print('Desenvolvendo uma PA(progressão aritmética), em 10 termos!!!)')

s = float(input('Digite o valor INICIAL da sua PA: '))
r = float(input('Digite o valor da RAZÂO para a sua PA: '))

for i in range(1,11):
    print('O {}ª termo da sua PA sera: "{}"'.format(i,r*i+s))
