print('Digite os dados de 4 pessoas!!!\n')
r = {}
n = {}
f = {}
m = []
l = {}
for i in range(0,4):
    r[i] = input('Digite o Nome da {}º pessoa: '.format(i+1))
    n[i] = int(input('Digite a idade da {}º pessoa: '.format(i + 1)))
    f[i] = input('Digite o sexo da {}º pessoa(M/F): '.format(i + 1))
    l[i] = [r[i], n[i], f[i]]
    m.append(l[i])
midade = 0
hv = 0
hn = ''
qm20 = 0
for i in range(0, 4):
    midade = midade + int(m[i][1])
    if str(m[i][2]) == 'M' or str(m[i][2]) == 'm' and hv < int(m[i][1]):
        hn = m[i][0]
    if int(m[i][1]) < 20 and m[i][2] == 'F' or m[i][2] == 'f':
        qm20 = qm20 + 1
print('A média de idade do grupo é : {}'.format(midade/4))
print('O nome do homem mais velho é : {}'.format(hn))
print('A quantidade de mulheres com menos de 20 anos é de : {}'.format(qm20))
print('Fim de Script')