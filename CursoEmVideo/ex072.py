print('número por extenso')
le = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',  'sete', 'oito', 'novo', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte',]

r = -1
while r not in range (0,21):
    r = int(input('Digite um valor entre "0" e "20": '))
    if r < 0 or r > 20:
        print('Digite um valor entre o parâmetros informado...')


print(f'O númerio {r} por extenso é "{le[r]}" ')
