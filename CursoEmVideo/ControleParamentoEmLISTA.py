m = [['ll', 32, 'F'], ['pp', 15, 'F'], ['oo', 40, 'M'], ['ff', 15, 'F']]

print(m[0][1], m[1][1] , m[2][1] ,m[3][1])

midade = 0
hv = 0
hn = ''
qm20 = 0

for i in range(0, 4):
    midade = midade + int(m[i][1])
    if str(m[i][2]) == 'M' or str(m[i][2]) == 'm' and hv < int(m[i][1]):
        hn = m[i][0]
    if m[i][2] == 'F' or m[i][2] == 'f' and int(m[i][1]) < 20:
        qm20 = qm20 + 1

print('A média de idade do grupo é : {}'.format(midade/4))
print('O nome do homem mais velho é : {}'.format(hn))
print('A quantidade de mulheres com menos de 20 anos é de : {}'.format(qm20))

print('Fim de Script')


