import time
def contagem(a, b , c):
    print('-='*10 + '=-'*10)
    if a > b and c > 0:
        c = c*(-1)
    if a < b:
        if c <= 0 or (a+c) > b:
            c = 1
    if a > b :
        if c >= 0 or (a+c) < b:
            c = -1
    ss = a
    if c >= 1:
        while ss <= b:
            print(f'{ss}', end=' ')
            ss = ss + c
            time.sleep(0.1)
            if ss > b:
                print('Fim')
    if c <= -1:
        while ss >= b:
            print(f'{ss}', end=' ')
            ss = ss + c
            time.sleep(0.1)
            if ss < b:
                print('Fim')
    print('-='*10 + '=-'*10)

print('-='*10 + '=-'*10)

contagem(1, 10 ,1)
contagem(10, 1 ,-1)

print('Agora é sua vez de personalizar a contagem!!!')
vri = int(input('Início: '))
vrf = int(input('Final : '))
vrc = int(input('Passo : '))

contagem(vri, vrf ,vrc)
