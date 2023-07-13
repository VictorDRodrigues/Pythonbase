import datetime
print('Programa de VERIFICAÇÃO de CLASSIFICAÇÂO de FAIXA ETARIA DE ATLETAS!!!')

datesystem = datetime.datetime.now()
ano = int(datesystem.strftime('%Y'))

n = int(input('Informe o ANO de nascimento do ATLETA (Ex: AAAA): '))

r = (n-ano)*-1

print('O ATLETA é classificado com tendo: {} anos de idade'.format(r))

if r <= 9:
    print('O Atleta é classificado na categoria MIRIM!!!')
elif r <= 14:
    print('O Atleta é classificado na categoria INFANTIL!!!')
elif r <= 19:
    print('O Atleta é classificado na categoria JUNIOR!!!')
elif r == 20:
    print('O Atleta é classificado na categoria SÊNIOR!!!')    
elif r < 20:
    print('O Atleta é classificado na categoria MASTER!!!')    

print('Fim do script.')
