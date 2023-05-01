turmas = int(input("Informe a quantidade de turmas: "))
alunos = []
for i in range(turmas):
    aluno = int(input(f"Informe a quantidade de alunos na {i+1}° turma: "))
    alunos.append(aluno)
print(f"A media de aluno por turma seria {int(sum(alunos) / turmas)}")
