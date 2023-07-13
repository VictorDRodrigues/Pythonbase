le = []
li = []
lp = []
x = 0
xi = 0
xp = 0
rr = 'S'
rc = 0.0
#cria um range infinito ate que receba respota negativa, no caso vai ser 'N' ou 'n'
while rr in 'SsNn':
    #valor i a ser avaliado e incrementado.
    i = int(input(f'Digite {x+1}ª valor inteiro(sem casa decimal) para a lista de valores: '))
    #se for o primeiro número adiciona ele na consição if, se não entra no else e verifica valor
    le.append(i)
    # verificar o user deseja continuar, so sai com resposta S ou N
    rr = str(input('Quer continuar a adicinar valores para a lista?[S/N]'))
    while rr not in 'SsNn':
        rr = str(input('Quer continuar a adicinar valores para a lista?[S/N]'))
    # se caso receba uma resposta negativa pare de incremental de finalize loop infinito
    if rr in 'Nn':
        break
print('='*30)
print(f'len {len(le)}')
#linha de codigo que utiliza metodo de aninhamento, para criação de números IMPARES
li = [xi for xi in le if float(xi%2) > 0]
print(f'li {li}')
#linha de codigo que utiliza metodo de aninhamento, para criação de números PARES
lp = [xp for xp in le if float(xp%2) == 0]
print(f'lp {lp}')

# print do total de valores dentro a listas
print(f'Os VALORES dentro lista PRINCIAPL ficou da seguinte maneira {le}')
print(f'Os VALORES dentro lista PAR ficou da seguinte maneira {lp}')
print(f'Os VALORES dentro lista IMPAR ficou da seguinte maneira {li}')

print('Fim de adicão de valores para lista...')    
