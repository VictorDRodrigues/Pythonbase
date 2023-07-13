print('Desenvolvendo uma PA(progressão aritmética), em 10 termos!!!)')

s = float(input('Digite o valor INICIAL da sua PA: '))
r = float(input('Digite o valor da RAZÂO para a sua PA: '))

i = 1

print('O seu valor Inicial é "{}"'.format(s))
while i <= 10:
    print('O {}ª termo da sua PA sera: "{}"'.format(i,r*i+s))
    i = i + 1

print('Fim do ')

