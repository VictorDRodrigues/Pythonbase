print('Desenvolvendo uma PA(progressão aritmética), em 10 termos!!!)')

s = float(input('Digite o valor INICIAL da sua PA: '))
r = float(input('Digite o valor da RAZÂO para a sua PA: '))

i = 1
a = 0
ct = 0

print('O seu valor Inicial é "{}"'.format(s))
while i <= 11:
    print('O {}ª termo da sua PA sera: "{}"'.format(i,r*i+s))
    i = i + 1
    c = int(i) 
    while i == 11:
        rr = str(input('Deseja Continuar vendo mais termos da sua PA?(S \ N) '))
        if rr.upper() == 'S':
            a = int(input('Deseja aumentar a PA me quantos temos? '))
            ct = c + a
            while c != ct:
                print('O {}ª termo da sua PA sera: "{}"'.format(c,r*c+s))
                c = c + 1
        if rr.upper() == 'N':
            i = i + 1

print('Fim do script ')

