import random
print('Jogo da advinhação, entre p número 0 e 10!!!')

mr = int(random.randint(0, 11))
r = -1
c = 0
while (mr != r) :
    r = int(input('Digite o Valor da sua resposta: '))
    c = c + 1
print('Parabens vc Acertor, em {} tentativas'.format(c))
