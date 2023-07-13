import math

print('soma dos número imppares, que sao multiplos de 3, de 1 a 500')
ic = 0
cc = 0
for i in range(1,501,2):
    #if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 9 != 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0:
    if i % 3 == 0:
        ic = ic + i
        cc = cc + 1
        print('{}'.format(i))
print('Fim ic: {} e cc: {}'.format(ic,cc))