def area(a, b):
    ss = float(a) * float(b)
    print(f'A área de um terrono {a}x{b} é de {ss}m²')

print('Controle de Terreno')
print('-='*10 + '=-'*10)
largura = float(input('LARGURA (Metros): '))
altura = float(input('ALTURA (Metros): '))
area(largura,altura)
