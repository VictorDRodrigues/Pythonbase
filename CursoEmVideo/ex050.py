n = {}
r = 0
for i in range (1,7):
    n[i] = input('Digite {}ª número entre uma lista de 6 números: '.format(i))
    if int(n[i]) % 2 == 0:
        r = r + int(n[i])
print(n)
print('Basedo nos valores informados\nO total da soma de todos os valores pares é de "{}"'.format(r))
#for i in range (1,7):
    
