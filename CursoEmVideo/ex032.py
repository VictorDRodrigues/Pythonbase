d = int(input('Digite o ANO que deseja saber se é Bissexto: '))

bd= int(d%4)

print ('O ano de {} é Bissexto.'.format(d) if bd == 0 else 'O ano de {} NÂO é Bissexto.'.format(d))

