a = float(input("Digite o valor de A: "))

def calc(a):
    if a == 0:
        print("Sua equação não é do segundo grau")
        return False
    else:
        x = float(input("Informe o valor de X: "));
        b = float(input("Informe o valor de B: "));
        c = float(input("Informe o valor de C: "))
        delta = a * x ** 2 + b * x + c;
    if delta < 0:
        print("A equação não possui raizes reais")
        return False
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
        return False
    elif delta > 0:
        print("A equação possui duas raiz reais");
calc(a)

