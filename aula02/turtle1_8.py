import turtle

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

# Cor para o quadrado
tartaruga.fillcolor("light cyan")
tartaruga.begin_fill()

# Desenhando um quadrado
for i in range(4):
    tartaruga.forward(200)
    tartaruga.left(90)

# Terminando de desenhar um quadrado
tartaruga.end_fill()

# cor para o círculo
tartaruga.fillcolor("pink")
tartaruga.begin_fill()

# Desenhando um círculo
tartaruga.forward(100)
tartaruga.circle(50)

# Terminando de desenhar um círculo
tartaruga.end_fill()