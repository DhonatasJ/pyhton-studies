# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário
# e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

data_nasc = input("Insira a data de nascimento no foramro (dd/mm/aaaa): ")

def nasc(data_nasc):
    dia, mes, ano = data_nasc.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    meses = {
        1:"Janeiro",
        2:"Fevereiro",
        3:"Marco",
        4:"Abril",
        5:"Maio",
        6:"Junho",
        7:"Julho",
        8:"Agosto",
        9:"Setembro",
        10:"Outubro",
        11:"Novembro",
        12:"Dezembro",
    }
    return f"Você nasceu em  {dia} de {meses[mes]} de {ano}"

print(nasc(data_nasc))