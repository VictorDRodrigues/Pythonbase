n = input('Digite o nome completo: ').upper().capitalize()

s = n.split()
c = len(s)

print('O Primeiro nome é {}'.format(s[0]))
print('O ultimo nome é {}'.format(s[c-1]))
