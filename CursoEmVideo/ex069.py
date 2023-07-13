print('Cadastro de pessoas e resumo dos cadastros')
ht = y18 = y20 = 0
while True:
    y = int(input('Digite idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Digite sexo(M/F): '))
    if y >= 18:
        y18 = y18 + 1
    if s == 'M':
        ht = ht + 1
    if y < 20 and s == 'F':
        y20 = y20 + 1

    r = ' '
    while r not in 'SN':
        r = str(input('Digite sexo(S/N): '))
    if r == 'N':
        break

print('Total de Adultos com mais de 20 anos {}'.format(y18))
print('Total de Mulheres com mais de 20 anos {}'.format(y20))
print('Total de homens {}'.format(ht))
print('Fim do Script')