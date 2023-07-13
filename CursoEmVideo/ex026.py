n = input('Digite sua frase: ').upper().strip()

r1 = n.count('A')
r2 = n.find('A')
r3 = n.rfind('A')

print('A quantidade de letras "A" é de : {}'.format(r1))
print('A posição do primeira letras "A" é : {}'.format(r2+1))
print('A posição da ultima letras "A" é : {}'.format(r3))