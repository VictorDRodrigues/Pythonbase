le = []
x = 0
lm = [0]
Ln =[99999999999999999999999999999999]
while x in range(0,5):
    le.append(int(input(f'Digite um valor para a Posição "{x:.0f}": ')))
    x = x + 1

x = 0
while x in range(0,5):
    if le[x] > lm[0]:
        while lm[0] in lm:
            lm.remove(le[0])
    elif le[x] == lm[0]:
        le.append(le[x])
    print(le)

print(le)
