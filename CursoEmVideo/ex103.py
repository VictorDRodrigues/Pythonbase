
def ficha(nome='desconhecido', gols=0):
    le = {}
    le = (f'"nome": {nome}, "gols": {gols}')
    return le

nome = input('Digite o Nome do Jogador: ')
gols = input('Digite o Números de gols: ')
ll = []
print(f'nome: {nome}')
print(f'gols: {gols}')

ll = ficha(nome, gols)
if nome == '' and gols == '':
    ll = ficha() 
elif nome == '':
    ll = ficha(gols = gols)
elif gols == '':
    ll = ficha(nome = nome)
print('Mostra ll...')
print(f'{ll}')



