print('Verificador de PALÍNDROMO!!!')
print('Exemplo: "OVO" , "ANA" , "APOSASOPA"')
r = input('Digite uma frase ou palavras que jugue ser um palíndromo:\n')
r = r.replace(' ','')
c = len(r)
print('Tamanho do palindromo: "{}"'.format(c))

p = 1
for i in range(0,c):
    if r[i] == (r[int(c) - i -1]):
        p = 1
    else:
        p = 0

if p == 1:
    print('"{}" é um PALINDROMO'.format(r))
else:
    print('"{}" NÂO é um PALINDROMO'.format(r))


