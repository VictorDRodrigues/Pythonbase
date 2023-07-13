import random

alunos = []
quantidade_alunos = 4

for i in range(quantidade_alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    alunos.append(nome)

posicoes = list(range(1, quantidade_alunos + 1))
random.shuffle(posicoes)

for posicao, aluno in zip(posicoes, alunos):
    print(f"O aluno escolhido para apresentar em {posicao}º lugar é {aluno}")
