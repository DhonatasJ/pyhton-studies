class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura    
    
    def envelhecer(self):
        if self.idade < 21:
            for i in range(21 - self.idade):
                self.idade += 0.05
        return round(self.idade,2)
    
    def engordar(self):
        return self.peso
    
    def emgrecer(self):
        return self.peso
    
    def crescer(self):
        return self.altura
    
p1 = Pessoa("Jorginho", 12, 72.5, 1.82)        

print(p1.envelhecer())
print(p1.engordar())
print(p1.emgrecer())
print(p1.crescer())





# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa 
# envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.