
alnAlto = 0
alnBaixo = float('inf')
nmrAlunoA = 0
nmrAlunoB = 0
for i in range(10):
    n,a = input("Insira o numero do aluno e sua altura separados por virgulas: ").split(",")
    n,a = int(n), float(a)
    if alnAlto < a:
        alnAlto = a
        nmrAlunoA = n
    if alnBaixo > a:
        alnBaixo = a
        nmrAlunoB = n

print("O aluno N⁰ {} é mais baixo com {} de altura".format(nmrAlunoB, alnBaixo))
print("O aluno N⁰ {} é mais alto {} de altura".format(nmrAlunoA, alnAlto))
