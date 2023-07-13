le = []
x = 0
#cria um range de 5 posições
while x in range(0, 5):
    #valor i a ser avaliado e incrementado.
    i = int(input(f'Digite {x+1}ª valor inteiro para a lista de valores: '))
    #se for o primeiro número adiciona ele na consição if, se não entra no else e verifica valor
    if x == 0:
        le.append(i)
    else:
        #zera valor de xo, cria range do tamanho da lista atual.
        xo = 0
        while xo in range(0, len(le)):
            #1ª condicionalverifica se o número e menor e coloca ele na posição do número que esta sendo avaliado.
            if i < int(le[xo]):
                le.insert(xo, i)
                break
            #2ª condicional verifica se o número esta no ultimo número da lista e coloca ele ao final da lista
            if xo == int(len(le)-1):
                le.append(i)
                break
            # contador de xo
            xo = xo + 1
    # contador de x
    x = x + 1
print(f'Os valores ordenado nas lista fica da segunte maneira:')
print(le)
print('Fim de adicão de valores para lista...')    
