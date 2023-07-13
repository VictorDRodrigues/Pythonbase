import datetime
def voto(yborn):
    dat = datetime.datetime.now() # busca data da sistema
    ynow = dat.year # busca somente o parte relaciona ao ANO (YYYY)
    if ynow < yborn:
        return print('NEGADO, mas você ainda não NASCEU!')
    elif ynow == yborn:
        return print('NEGADO, você NASCEU neste ANO.')
    else:
        yu = ynow - yborn 
        #print(f'{yu}') #printa idade mas é desnecessario para função ocorrer
        if yu < 16:
            return print(f'Com {yu} anos de idade: NEGADO, menor de 16 anos de idade.')
        elif yu >= 16 and 18 > yu:
            return print(f'Com {yu} anos de idade: OPCIONAL, maior de 16 e menoer de 18 anos.')
        elif yu >= 65:
            return print(f'Com {yu} anos de idade: OPCIONAL, maior de 65 anos.')
        else:
            return print(f'Com {yu} anos de idade: OBRIGATÓRIO.')
            
    
print('Validador de situação eleitoral por funcção. 1 Função(sorteia)')
r = int(input('Digite o Ano de Nascimento(YYYY): '))
print('Analisando os Dados informados... \nSua obrigação eleitoral é ')
voto(r)

