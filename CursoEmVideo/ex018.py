import math
ang = float(input('Digite um valor do angulo do seu Triangulo: '))

ase = math.sin(math.radians(ang))
aco = math.cos(math.radians(ang))
ata = math.tan(math.radians(ang))


print('O valor de seno é {:.2f}'.format(ase))
print('O valor de cosseno é {:.2f}'.format(aco))
print('O valor de tangente é {:.2f}'.format(ata))