import random
def sorteia(números):
    i = 0
    while i != 5:
        intnumero = random.randint(0,9)
        números.append(intnumero)
        #print(f'Número adicionado foi {intnumero}')
        i = i + 1
    return números

def somaPar(números):
    somaPar = 0
    for i in números:
        vPar = float( i % 2)
        if vPar == 0:
            somaPar = somaPar + i
            #print(f'somaPar {i}')
    return print(f'Somando os valores pares de {números}, temos {somaPar}')




print('Sorteia 5 números aleatorios, adicona na em uma lista. 1 Função(sorteia)')
print('Verifica dentro da lista,\nquais números são pares e soma os números pares. 2 Função(SomaPar)')
números = []
sorteia(números)
print(f'Sorteando {len(números)} valores da lista: {números}')
somaPar(números)
