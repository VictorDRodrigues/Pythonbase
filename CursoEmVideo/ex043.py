print('Programa de VERIFICAÇÃO de IMC(Indice de Massa Corporal)!!!')

a = float(input('Informe a altura(exemplo: 1.99): '))
p = float(input('Informe o Peso(exemplo: 99.99): '))

r = p/(a**2)

print('O IMC deu o valor de: "{:.2f}"'.format(r))

if r < 18.5:
    print('O IMC é classificado como : ABAIXO DO PESO!!!')
elif r > 18.5 and r <= 25:
    print('O IMC é classificado como : PESO IDEAL!!!')
elif r > 25 and r <= 30:
    print('O IMC é classificado como : SOBREPESO!!!')
elif r > 30 and r <= 40:
    print('O IMC é classificado como : OBESIDADE!!!')
elif r > 40:
    print('O IMC é classificado como : OBESIDADE MÓRBIDA!!!')

print('Fim do script.')
