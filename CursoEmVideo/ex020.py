import random

n1 = str(input('Digite o Nome do primeiro aluno: '))
n2 = str(input('Digite o Nome do segundo aluno: '))
n3 = str(input('Digite o Nome do terceiro aluno: '))
n4 = str(input('Digite o Nome do quarto aluno: '))

ltamanho = 4
linc_i = 1
lfin_i =4

lrng = random.sample(range(linc_i, lfin_i + 1), ltamanho)

print(lrng)

for i in range(ltamanho):
    if lrng[i] == 1:
        r = n1
    elif lrng[i] == 2:
        r = n2
    elif lrng[i] == 3:
        r = n3
    else:
        r = n4
    print("O Aluno escolhido para apresentar em {} lugar, é o {}".format(i+1, r))


