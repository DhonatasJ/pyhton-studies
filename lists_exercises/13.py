
monthAndTemp = {}
while True:
    month = input("Informe o mes que deseja passar a temperatura, ou 'fim' para finalizar: ")
    if month == 'fim':
        print("Consulta encerrada!")
        break
    temp = input("Informe a temperatura: ")
    monthAndTemp[month] = temp
print(monthAndTemp)