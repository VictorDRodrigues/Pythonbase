print('Programa de converção de type base!!!')
n = int(input('Digite o valor inteiro(número sem casas decimais): '))

r = int(input('Escolhas entre as opções a seguir:\n1 - Para Binário.\n2 - Para Octal.\n3 - Para Hexadecimal\n'))
rr = 0
if r == 1:
    rr = bytes(n)
    print('{}'.format(rr))
elif r == 2:
    rr = oct(n)
    print('{}'.format(rr))
elif r == 3:
    rr = hex(n)
    print('{}'.format(rr))
else :
    quit()
