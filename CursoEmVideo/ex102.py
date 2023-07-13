
def fatorial(número, show=False):
    """
Fatorial (, show=False)
  -> Calcula o Fatorial de um número.
  :Param n: O número a ser calculado.
  :Param show: (opcional) Mostra ou não a conta.
  :return: O valor do Fatorial de um número n.
"""
    f = número
    for i in range(número, 0, -1):
        if i == 1 and show == True:
            print('1 = ', end='')
            break
        elif show == True:
            print(f'{i} x ', end='')
            f = f *(i-1)
            i = i - 1
        else:
            if i == 1:
                break
            f = f *(i-1)
            i = i - 1
    return f




    
print('Mostra FATORIAL deu um número...')
r = int(input('Digite o valor FATORIAL: '))
f = fatorial(r, show=True)
#f = fatorial(r)
print(f'{f}')
#help(fatorial)


