import datetime
salario_inicial = float(input("Insira o salario do colaborador: "))
ano_inicial = int(input("Insira o ano em que o colaborador comecou: "))
ano_final = datetime.datetime.now().year
percentual = 1.5
percent = 0
salarioUp = 0
for i in range(ano_inicial, ano_final):
    percentual *= 2
    salarioUp = salario_inicial + ((salarioUp / 100) * percentual)
    print(salarioUp)

