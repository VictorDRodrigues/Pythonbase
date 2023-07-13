import random
print('Jogo de Impar/PAR')
print('======================')
print('Regra do Impar/PAR\n======================\nPrimeiramente escolha qual resultado vai dar se ele vai ser IMPAR ou PAR.\n'
'O resultado depende da soma do número que voçê escolheu com o número que a maquina escolheu.')
print('======================')
ct = 0

while True:
    print('======================')
    l = int(input('Entre:\n1 - Impar\n2 - Par\nQual opção você escolher: '))
    if l == 1:
        print('Voçê Escolheu IMPAR.')
        print('Você "IMPAR" x "PAR" MAQUINA.')
    elif l == 2:
        print('Você "PAR" x "IMPAR" MAQUINA.')
    else:
        print('SEM ESCOLHA VALIDA.')

    r = int(input('Digete qual número vc vai jogar: '))
    m = random.randint(1, 2)
    print('======Resultado=======')
    print(f'Você "{r}" x "{m}" MAQUINA. Total: {r+m}')
    if l == 2 and (r + m) % 2 == 0:
        print('Você Ganhou')
        print('======================')
        ct = ct + 1
    elif l == 1 and (r + m) % 2 > 0:
        print('Você Ganhou')
        print('======================')
        ct = ct + 1
    else:
        print('Você Perdeu..... GAME OVER')
        print('======================')
        break
print(f'Você obteve {ct} vitoria(s) consecutivas')
print('Final do Script')


