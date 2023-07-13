le = []
x = 0
lm = []
ln =[]
while x in range(0,5):
    le.append(int(input(f'Digite um valor para a Posição "{x:.0f}": ')))
    x = x + 1
x = 0
#print(le)
print('=-'*20)
xo = 0
while x in range(len(le)):
    if x == 0:
        lm.append(int(le[0]))
        ln.append(int(le[0]))
    else:
        if int(le[x]) > int(lm[0]):
            lm.pop()
            lm.append(int(le[x]))
        if int(le[x]) < int(ln[0]):
            ln.pop()
            ln.append(int(le[x]))
    x = x + 1
print(f'O maior valor digitado foi {lm[0]} na posição...', end='')
x = 0
while x in range(len(le)):
    if int(lm[0]) == int(le[x]):
        print(f' {x}...', end='')
    x = x + 1
print('')
print(f'O menor valor digitado foi {ln[0]} na posição...', end='')
x = 0
while x in range(len(le)):
    if int(ln[0]) == int(le[x]):
        print(f' {x}...', end='')
    x = x + 1

print('')

#print(f'le: {le}')
#print(f'lm: {lm}')
#print(f'ln: {ln}')
