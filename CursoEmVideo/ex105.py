
def notas(*num, sit=False):
"""
notas(*num, sit=False)
    -> Função para analise de notas e situações da media das notas
    :param n: * 1 ou mais n notas dos alunos
    :param sit:valor opcional, default False, se true mostra situação mais notas
    :return: DICT() com 'total de notas', 'MaiorNota', 'MenorNota' , 'Média' e se sit igual True adicional de 'Situação', 'Notas(todas as notas informadas)'
"""
    #criação de variaveis da função
    le = dict()
    c = 0
    notasoma = 0
    maxnota = 0
    minnota = 10
    # verificando cada item dentro do loop de nodas.
    while c in range (0, int(len(num))):
        #soma total de notas
        notasoma = notasoma + num[c]
        # valida MIN MAX DE NOTAS
        if num[c] > maxnota:
            maxnota = num[c]
        if num[c] < minnota:
            minnota = num[c]
        # Contador do loop
        c = c +1
    # Calculo e desenvolvimento de METADADOS
    media = round(notasoma/int(len(num)), 2)
    situacao = ''
    if media > 9:
        situacao = 'Muito Boa!'
    elif media >= 7 and media < 9:
        situacao = 'Boa!'
    elif media >=6 and media < 7:
        situacao = 'Regular!'
    elif media >=3 and media < 6:
        situacao = 'Ruim.'
    else:
        situacao = 'Critica!!!'
    #criação do Dicionario completo
    if sit == True:
        le = {
            'total': len(num),
            'maiornota': maxnota,
            'menornota': minnota,
            'media': media,
            'situação': situacao,
            'notas': num
            }
    else:
        le = {
            'total': len(num),
            'maiornota': maxnota,
            'menornota': minnota,
            'media': media,
            }
    return le

le = []
#le = notas(5.7, 9.3, 6.5 , 7.8)
le = notas(5.7, 9.3, 6.5 , 7.8, sit= True)

print(le)
print(type(le))

print('Mostra resposta...')




