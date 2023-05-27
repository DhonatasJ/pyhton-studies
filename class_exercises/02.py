class Quadrado:
    def __init__(self, lateral):
        self.lateral = lateral

    def change_lateral(self, new_lateral):
        self.lateral = new_lateral

    def retorna_lateral(self):
        return self.lateral

    def calc_area(self):
        return self.lateral ** 2
ltrl = int(input("Insira o tamanho da lateral: "))
change_ltrl = int(input("Insira um numero diferente caso deseje mudar: "))
q1 = Quadrado(ltrl)

print(q1.retorna_lateral())
q1.change_lateral(change_ltrl)
print(q1.retorna_lateral())
print(q1.calc_area())

# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
