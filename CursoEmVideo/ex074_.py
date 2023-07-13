import random
print('Cria Tuplas randomicas')

x = 0
lr = (random.randint(1,10) , random.randint(1,10) ,random.randint(1,10) ,random.randint(1,10) ,random.randint(1,10))

print('===========================================')
print(f'Os Valores sorteados foram: ', end='')
for n in lr:
    print(f'{n}', end=' ')
print('\n===========================================')
print(f'O maior número é "{max(lr)}"')
print(f'O menor número é "{min(lr)}"')
