r = 0
le = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canete', 22.30,
    'Livro', 34.90
    )

print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)

while r in range(0,18):
    print(f'{le[r]:.<29}R${le[r+1]:>9.2f}')

    r = r + 2
