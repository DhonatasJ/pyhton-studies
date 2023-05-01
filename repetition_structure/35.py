intervalo1 = int(input("Insira que começa a verificação: "))
intervalo2 = int(input("Insira que termina a verificação: "))
list = []
for nmr in range(intervalo1, intervalo2+1):
    if nmr > 1:
        for i in range(2, nmr):
            if (nmr % i == 0):
                break
        else:
            list.append(nmr)
print(f"Os numeros primos no range informado é {list}")
