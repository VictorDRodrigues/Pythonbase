
def leiaint():
    ok = False
    valor = 0
    while True:
        r = str(input('Digite um valor: '))
        if r.isnumeric():
            valor = int(r)
            ok = True
        else:
            print('Erro Digite um número inteiro')
        if ok:
            break
    return valor

        
    

print('Validade de número inteiro')
resposta = leiaint()
print('Mostra resposta...')
print(f'{resposta}')



