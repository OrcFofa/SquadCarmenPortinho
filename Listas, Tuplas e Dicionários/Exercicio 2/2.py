# 2 Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

aluno = 1
medias = []
aprovados = 0

while aluno <= 5:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    print("-------------------------------")

    media = (nota1 + nota2 + nota3 + nota4) / 4

    medias.append(media)

    aluno +=1

for media in medias:
    if media >= 7:
        aprovados += 1


print(f"{aprovados} alunos obtiveram média maior ou igual a 7.0")