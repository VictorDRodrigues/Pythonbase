
km = float(input('Digite quanto KM foi percorrido com o carro '))

dia = int(input('Digite quantos DIA(s) foi alugado o carro '))

r = (0.15*km)+(60*dia)

print('O valor a ser pago do aluguel do carro é de {:.2f}'.format(r))
