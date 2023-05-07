valorPrestacao = float(input("Insira o valor da prestacao: "))
a_pagar = 0
def valorPgto(valorPrestacao, dias_atrasado):
    while True:
        if valorPrestacao == 0:
            print("Encerrando...")
            break
        else:
            a_pagar += valorPrestacao
            valorPrestacao = float(input("Insira o valor da prestacao: "))
            dias_atrasado = int(input("Dias em atraso: "))

print(a_pagar)