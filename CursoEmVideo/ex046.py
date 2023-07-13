import time

print('Aperte ENTER para dar inicio ao cronometro de 10 segundos')

for i in range(10, 0, -1):
    print('{}'.format(i))
    time.sleep(1)
print('Finish!')
