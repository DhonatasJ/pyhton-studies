class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
            
    def verBucho(self):
        if self.bucho == False: 
            print(f"{self.nome} esta com a barriga vazia...")
        else:
            print(f"{self.nome} esta com alguns alimentos no estomago")

    def digerir(self):
        if len(self.bucho) == 0:
            print("Nenhum alimento para ser digerido...")
        else:
            print(f"{self.nome} esta comendo {self.bucho}")
            self.bucho = []
            print(f"{self.nome} esta alimentado!")

macaco = Macaco("Jorginho")
macaco.comer("Banana")
macaco.comer("Maca")
macaco.comer("Batata")
macaco.comer("Ovo Frito")
macaco.verBucho()
macaco.digerir()

# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo 
# menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando 
# pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo 
# do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?