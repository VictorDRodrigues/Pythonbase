print("....Calculadora....")
r = 4
v1 = 0
v2 = 0
vr = 0
while r != 5:
    print("........MENU.......")
    print("1.......SOMA.......")
    print("2..MULTIPLICAÇÂO...")
    print("3......MAIOR.......")
    print("4..NOVOS..NÚMEROS..")
    print("5.SAIR.DO.PROGRAMA.")
    if r == 1:
        vr = v1 + v2
        print("A soma entre {} e {} é : {}".format(v1, v2, vr))
    if r == 2:
        vr = v1 * v2
        print("A mutiplicação entre {} e {} é : {}".format(v1, v2, vr))
    if r == 3:
        if v1 > v2:
            vr = v1
        else:
            vr = v2
        print("O maior número entre {} e {} é : {}".format(v1, v2, vr))
    if r == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))

    r = int(input('Informe qual ação vc deseja fazer do menu: '))

print('Final do Script')