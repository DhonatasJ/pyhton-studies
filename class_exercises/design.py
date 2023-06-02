import turtle

# Configurações iniciais da tela
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

# Configurações da tartaruga
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Função para desenhar um retângulo
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Função para desenhar um círculo
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Desenho da Mona Lisa
draw_rectangle(-200, 200, 400, 400, "lightgray")  # Fundo
draw_rectangle(-150, 100, 300, 200, "lightblue")  # Cabelo
draw_rectangle(-150, -100, 300, 200, "white")     # Rosto

# Olhos
draw_circle(-70, 50, 30, "black")    # Olho esquerdo
draw_circle(70, 50, 30, "black")     # Olho direito

# Nariz
draw_rectangle(-20, -20, 40, 80, "lightgray")  # Base do nariz
draw_circle(-20, 30, 20, "white")               # Ponta do nariz

# Boca
draw_rectangle(-70, -60, 140, 20, "red")    # Boca

# Sobrancelhas
draw_rectangle(-130, 150, 50, 20, "black")   # Sobrancelha esquerda
draw_rectangle(80, 150, 50, 20, "black")     # Sobrancelha direita

# Lágrimas
draw_circle(-90, -100, 10, "lightblue")     # Lágrima esquerda
draw_circle(90, -100, 10, "lightblue")      # Lágrima direita

# Laço
draw_rectangle(-60, -170, 120, 40, "lightblue")   # Faixa do laço
draw_rectangle(-20, -210, 40, 40, "lightblue")     # Nó do laço

# Assinatura
t.penup()
t.goto(180, -280)
t.color("black")
t.write("Leonardo da Vinci", align="center", font=("Arial", 12, "normal"))

# Esconder tartaruga
t.hideturtle()

# Manter a janela aberta
turtle.done()
