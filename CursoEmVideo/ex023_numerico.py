import math
n = int(input('Digite 1 número de 0 a 9999 : '))

u4 = n//1000 % 10
u3 = n//100 % 10
u2 = n//10 % 10
u1 = n//1 % 10

print('Unidade de Milhar : {}'.format(u4))
print('Unidade de Centena : {}'.format(u3))
print('Unidade de dezena : {}'.format(u2))
print('O valor de Unidade é de : {}'.format(u1))