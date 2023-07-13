print('Motra a Tabuado do número até x10, que for digitado, sai do programa se for negativo!!!')
r = 0
while True:
    r = int(input('Digite valor do qual deseja visuzalizar a tabuada? '))
    if r < 0:
        break
    t = 1
    print('----------------------------------------------------------')
    while t in range(1,11):
        print(f'{t} x {r} = {r * t}')
        t = t + 1
    print('----------------------------------------------------------')
print('Fim do Script')