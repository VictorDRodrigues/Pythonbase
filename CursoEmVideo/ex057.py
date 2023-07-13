r = 1
v1= v2 = ''
while r == 1:
    v1 = v2 = str(input('Digite o Sexo da pessoa(M/F): ')).upper()
    print(v1, v2, r)
    if v1 == 'M' or v2 == 'F':
        r = 0
print('Final do Script')