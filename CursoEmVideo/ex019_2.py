import random

alunos = []
quantidade_alunos = 4

for i in range(quantidade_alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    alunos.append(nome)

aluno_escolhido = random.choice(alunos)
numero_aleatorio = random.randint(1, 4)

print("O aluno escolhido foi o {}, número {}.".format(aluno_escolhido, numero_aleatorio))
