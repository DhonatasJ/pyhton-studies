def dataPorExtenso(data):
        dia = data[-1:-2]
        mes = data[-4:-5]
        ano = data[-7:-10]
        meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
        try:
            dia, mes, ano = map(int,data.split("/"))
            if not (1 <= dia <= 31 and 1 <= mes <= 12):
                    raise ValueError
            return f"Dia {dia} de {meses[mes]} de {ano}"
        except ValueError:
            return "NULL"

data = input("Insira a data no formato dd/mm/aaaa: ")
data1 = dataPorExtenso(data)
print(data1)