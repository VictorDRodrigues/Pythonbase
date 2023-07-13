
v = int(input('Digite a velocidade do carro: '))

va = (v - 80)
m = va * 7

if v <= 80:
    print('Você NÂO foi Multado!!! Pois estava a {}Km/h'.format(v))
else:
    print('Você FOI Multado!!! Pois estava a {},00Km/h'.format(v))
    print('O valor da Multado, é de {}R$.\nPois estava a {}Km/h a mais que 80km/h '.format(m,va))

print('Fim do script!')
