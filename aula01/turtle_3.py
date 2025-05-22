import turtle

def desenhar(x, y, w, h, cor):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(cor)
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

# Configuração inicial
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Desenhar a parede frontal (amarelo #FFC000)
desenhar(0, 0, 150, 100, "#FFC000")

# Desenhar a parede lateral (amarelo #FFC000)
t.penup()
t.setpos(0, 0)
t.pendown()
t.fillcolor("#FFC000")
t.begin_fill()
t.goto(-50, 50)
t.goto(-50, 150)
t.goto(0, 100)
t.goto(0, 0)
t.end_fill()

# Desenhar o telhado (face frontal #C0504D)
t.penup()
t.setpos(0, 100)
t.pendown()
t.fillcolor("#C0504D")
t.begin_fill()
t.goto(150, 100)
t.goto(100, 150)
t.goto(0, 100)
t.end_fill()

# Desenhar o telhado (face lateral #C00000)
t.penup()
t.setpos(0, 100)
t.pendown()
t.fillcolor("#C00000")
t.begin_fill()
t.goto(-50, 150)
t.goto(100, 150)
t.goto(0, 100)
t.end_fill()

# Desenhar a porta (laranja #FF8200)
desenhar(0, 0, 40, 60, "#FF8200")

# Desenhar as janelas (preto #000000)
desenhar(70, 20, 30, 20, "#000000")
desenhar(110, 20, 30, 20, "#000000")

# Ocultar o turtle e manter a janela aberta
t.hideturtle()
turtle.done()