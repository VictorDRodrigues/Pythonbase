import random

n1 = str(input('Digite o Nome do primeiro aluno: '))
n2 = str(input('Digite o Nome do segundo aluno: '))
n3 = str(input('Digite o Nome do terceiro aluno: '))
n4 = str(input('Digite o Nome do quarto aluno: '))

rng = random.randint(1, 4)
r = ''

if rng == 1:
    r = n1
elif rng == 2:
    r = n2
elif rng == 3:
    r = n3
else:
    r = n4

print("O Aluno escolhido foi o {}, {}".format(rng, r))