class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def result(self):
        return self.x, self.y
ponto = Ponto(24,52).result()
        
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
Retangulo(7.4, 3.2)
retangulo = Retangulo()

def result_ponto(ponto):
    print(ponto)

result_ponto(ponto)

def centro_retangulo(retangulo):
    


# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

# - Possua uma classe chamada Ponto, com os atributos x e y.
# - Possua uma classe chamada Retangulo, com os atributos largura e altura.
# - Possua uma função para imprimir os valores da classe Ponto
# - Possua uma função para encontrar o centro de um Retângulo.
# - Você deve criar alguns objetos da classe Retangulo.
# - Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, 
# que deve ser um objeto da classe Ponto.
# - A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique 
# os valores de x e y para o centro do objeto.
# - O valor do centro do objeto deve ser mostrado na tela
# - Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.