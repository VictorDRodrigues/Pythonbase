print('Progama de somatorio de números inteiros!!!(Digite 999 para sair)')
n = 0
r = 0
while r != 999:
    r = int(input('Digite valor: '))
    n = n + r

print("O valor total final menos 999 do comando para sair é de: {}".format(n-999))