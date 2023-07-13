import math

real = float(input('Digite um valor Real qualquer: '))

t = math.trunc(real)

print('A parte inteira de {} é {:.0f}'.format(real,t))