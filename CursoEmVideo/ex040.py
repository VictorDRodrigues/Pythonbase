import datetime
print('Programa de VERIFICAÇÃO de NOTA de Aluno!!!')
n1 = float(input('Digite a 1ª NOTA da PROVA.(X.X): '))
n2 = float(input('Digite a 2ª NOTA da PROVA.(X.X): '))
nv = (n1+n2)/2

print('O Avaliado teve média de NOTA: {},'.format(nv))

if nv >=7:
    print('O avaliado esta APROVADO!!!')
elif nv < 5:
    print('O avaliado esta REPROVADO!!!')
elif nv >= 5 and nv <= 6.9:
    print('O avaliado esta de RECUPERAÇÂO!!!')
print('Fim do script.')

