print('Progama de somatorio de números inteiros!!!(Digite 999 para sair)')

nt = c = 0
while True:
    r = int(input("Digite um valor inteiro: "))
    if r == 999:
        break
    c = c + 1
    nt = nt + r

print(f"O total é de '{nt}'")
print(f"O total de números é '{c}'")
