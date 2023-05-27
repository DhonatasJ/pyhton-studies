class Bola:

    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def change_color(self, nova_cor):
        self.cor = nova_cor

    def show_color(self):
        return self.cor

# Classe Bola: Crie uma classe que modele uma bola

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

bola = Bola('Black', 180, 'couro')
print("Orgin color: " + bola.show_color())
bola.change_color('White')
print("Color changed: "+ bola.cor)
