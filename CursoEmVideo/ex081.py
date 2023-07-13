le = []
x = 0
rr = 'S'
#cria um range infinito ate que receba respota negativa, no caso vai ser 'N' ou 'n'
while rr in 'SsNn':
    #valor i a ser avaliado e incrementado.
    i = int(input(f'Digite {x+1}ª valor inteiro(sem casa decimal) para a lista de valores: '))
    #se for o primeiro número adiciona ele na consição if, se não entra no else e verifica valor
    if x == 0:
        le.append(i)
    else:
        #zera valor de xo, cria range do tamanho da lista atual.
        xo = 0
        while xo in range(0, len(le)):
            #1ª condicionalverifica se o número e maior e coloca ele na posição do número que esta sendo avaliado.
            if i > int(le[xo]):
                le.insert(xo, i)
                break
            #2ª condicional verifica se o número esta no ultimo número da lista e coloca ele ao final da lista
            if xo == int(len(le)-1):
                le.append(i)
                break
            # contador incremental do xo
            xo = xo + 1
    # verificar o user deseja continuar, so sai com resposta S ou N
    rr = str(input('Quer continuar a adicinar valores para a lista?[S/N]'))
    while rr not in 'SsNn':
        rr = str(input('Quer continuar a adicinar valores para a lista?[S/N]'))
    # se caso receba uma resposta negativa pare de incremental de finalize loop infinito
    if rr in 'Nn':
        break
    # contador incremental do x
    x = x + 1
# print do total de valores dentro a lista
print(f'A quantidade toltal de VALORES dentro lista são de "{len(le)}"')
#print da lista como se encontra após loop infinito e parada com resposta 'N' ou 'n'
print(f'Os valores ordenado em ordem decrescente na lista fica da segunte maneira: ')
print(le)
# verificar se existe o valor 5 dentro da lista, se sim entra em loop e mostra valores, caso não msg de n esta contido dentro da lista.
if 5 in le:
    print(f'O valor número "5" se encontra na sequente posição"', end=' ')
    x = 0
    while x in range(0, len(le)):
        if int(le[x]) == 5:
            print(f'{x+1}', end='... ')
        x = x + 1
    print('')
else:
    print('O valor número "5" não esta contido dentro da Lista.')
print('Fim de adicão de valores para lista...')    
