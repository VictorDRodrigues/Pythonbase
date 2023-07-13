import time
import random
def maior(num):
    print('-='*10 + '=-'*10)
    ax = 0
    i = 0
    tl = len(num)
    v = 0
    print('Analisando os valores passados...')
    #print(f'{num} ')
    for i in num:
        print(f'{i}', end=' ')
        if ax < i:
            ax = i
        i = i + 1
    print(f'Foram informados {tl} valores ao todo.')
    print(f'O maior valor informado foi {ax}.')
    print('-='*10 + '=-'*10)
    return 

p1= dict()
p2= dict()
p3= dict()
p4= dict()
p5= dict()
p1 = [2, 9, 4, 5, 7, 1]
p2 = [4, 7, 0]
p3 = [1, 2]
p4 = [6]
p5 = []
maior(p1)
maior(p2)
maior(p3)
maior(p4)
maior(p5)

