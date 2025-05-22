import turtle

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("aquamarine")
tartaruga.pencolor("blue")
tartaruga.speed(10)

# Desenha um círculo e dá 3 voltas
for step in range(0, 90):
    tartaruga.forward(10)
    tartaruga.left(4)
    # A cada 10 passos
    if step%10 == 0:
        tartaruga.stamp()
        
# Limpando tela
tartaruga.clear()