print('Digite 4 valores inteiros...')
x = r9 = r3 = 0

le = ( str(input('Digite qualquer valor númerico para o 1ª valor:')),
            str(input('Digite qualquer valor númerico para o 2ª valor:')),
                  str(input('Digite qualquer valor númerico para o 3ª valor:')),
                        str(input('Digite qualquer valor númerico para o 4ª valr:'))
      )

print(le)
r9 = le.count("9")
if le.count("3") < 1:
    r3 = 0
else:
    r3 = le.index("3") + 1
print(f'A quantidade de vezes que o número "9" aparece são: {r9}')
print(f'A posição do primeiro número "3" que aparece é na: {r3}ª posição')

while x in range(0,4):
    if int(le[x]) % 2 == 0:
        print(f'O número {le[x]} é PAR')
    x = x + 1
