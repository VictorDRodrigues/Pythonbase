import time
print('Avaliador de Aposentadoria')
le = dict() #Dicionario para verifica do DADO do JOGADOR.
ll = list() #Lista com os dados da partida.
x = 0
le['nome'] = str(input(f'Nome: '))
le['idade'] = int(input(f'Ano de Nascimento: '))
le['carteira'] = int(input(f'Carteira de Trabalho(0 não tem): '))
if le['carteira'] != 0:
    le['contratação'] = int(input(f'Ano de contratação: '))
    le['salário'] = float(input(f'Salário: R$ '))
ll.append(le.copy())
print('-='*10 + 'Dados', end='')
print('=-'*10)
print(f'Nome tem o valor {ll[0]["nome"]}')
print(f'Idade tem o valor {ll[0]["idade"]}')
print(f'Ctps tem o valor {ll[0]["carteira"]}')
print(f'Contratação tem o valor {ll[0]["contratação"]}')
print(f'Salário tem o valor {ll[0]["salário"]}')
if le['carteira'] != 0:
    a = (ll[0]["contratação"] + 35 ) - ll[0]["idade"]
    print(f'Aposentadoria tem o valor {a}anos')
print('-='*10 + '           ', end='')
print('=-'*10)
print('Final do Script')
