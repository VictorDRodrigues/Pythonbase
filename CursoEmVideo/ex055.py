print('Digite o peso de 5 pessoas(em Kg):\n')

r = {}
mai = -9999999999
men = 9999999999

for i in range(0,5):
    r[i] = float(input('Digite o {}º peso(Kg): '.format(i+1)))
    if float(r[i]) >= mai:
        mai = float(r[i])
    if float(r[i]) <= men:
        men = float(r[i])

print('A pessoa com maior peso tem "\033[31m{:.2f}\033[m" e a pessoa com menor peso tem: "\033[36m{:.2f}\033[m"'.format(mai,men))