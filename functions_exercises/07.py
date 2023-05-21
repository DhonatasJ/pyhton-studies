def valorPagamento(valorParcela, diasAtrasados):
    if valorParcela <= 0:
        return 0
    else:
        valorMulta = valorParcela * 0.03
        valorJuros = valorParcela * (0.001 * diasAtrasados)
        valorTotal = valorParcela + valorMulta + valorJuros
        return valorTotal
        
pagamentosRealizados = []
valorRecebido = float

while True:
    valorParcela = float(input("Insira o valor da parcela, ou digite \"0\" para sair: "))

    if valorParcela == 0:
        print("\nRelatorio do dia")
        print(f"{len(pagamentosRealizados)} Pagamentos realizados")
        print(f"Valor recebido {valorRecebido}")
        break
    diasAtrasados = int(input("Insira os dias em atraso: "))
    valorPagar = valorPagamento(valorParcela, diasAtrasados)
    pagamentosRealizados.append(valorPagar)
    valorRecebido += valorPagar
    print(f"Valor a ser pago: R$ {valorPagar:.2f}")