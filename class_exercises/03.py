class Retangulo:
    def __init__(self, base, altura, ):
        self.base = base
        self.altura = altura

    def muda_lado(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def valor_lados(self):
        return self.base, self.altura

    def calc_area(self):
        return (self.base * self.altura) / 2

    def calc_perimetro(self):
        return 2 * (base + altura)


base = float(input("Informe a vertical do local: "))
altura = float(input("Informe a horizontal do local: "))


retangulo = Retangulo(base, altura)

area = retangulo.calc_area()
perimentro = retangulo.calc_perimetro()

print(f"Sera necessario {area} metros quadrados de piso")
print(f"Sera necessario {perimentro} metros quadrados de rodape")


