import datetime
print('Digite o ano de nascimento de 7 pessoas:\n')
r = {}
ar = 0
aa = datetime.datetime.now().year

for i in range(0,7):
    r[i] = int(input('Digite o {}º ano(AAAA): '.format(i+1)))
    if int(r[i])+17 <= aa:
        ar = ar + 1

print('A quantidade de pessoas que são maiores de 18 anos é igual \033[36m"{}"\033[m'.format(ar))