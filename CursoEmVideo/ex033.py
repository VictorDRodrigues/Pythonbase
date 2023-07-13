d = []
n1 = int(input('Digite o primeiro número qualquer: '))
d.append(n1)
n2 = int(input('Digite o segundo número qualquer: '))
d.append(n2)
n3 = int(input('Digite o terceiro número qualquer: '))
d.append(n3)

d.sort()
print('Ordenando de modo crescente... ')

for i in range(3):
    print ('O {}º valor é "{}".'.format(i + 1, d[i]) )

