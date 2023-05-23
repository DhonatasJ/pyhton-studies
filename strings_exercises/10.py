numero = int(input("Insira um numero ate 99: "))

def por_extenso(numero):
    unidades = ["zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove"]
    diferentes = ["dez","onze","doze","treze","quartoze","quinze","dezesseis","dezesete","dezoito","dezenove"]
    dezenas = ["dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
    
    n1 = str(numero[-1])
    n2 = str(numero[-2])
    if numero >= 0 and numero <= 9:
        print(unidades[numero])
    elif numero >= 10 and numero <= 19:
        print(diferentes[numero-10])
    elif numero >= 20 and numero <= 99:
        print(f"{dezenas[n1]} e {unidades[n2]}")
        
resultado = por_extenso(numero)
print(resultado)