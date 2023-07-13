import datetime
print('Programa de VERIFICAÇÃO de TEMPO para ALISTAMENTO MILITAR!!!')
n1 = int(input('Digite o ANO de NASCIMENTO do avaliado(AAAA): '))
aa = n1 + 18

datesystem = datetime.datetime.now()
ano = int(datesystem.strftime('%Y'))

print('Este Ano de {},'.format(ano))

if ano == aa:
    print('O avaliado deve se apresentar para alistamento')
elif ano > aa:
    print('já se passou {} ano(s), para o avaliado se apresentar para o alistamento'.format(ano-aa))
elif ano < aa:
    print('Ainda falta {} ano(s), para o avaliado se apresentar para o alistamento'.format(aa-ano))
    
print('Fim do script.')

