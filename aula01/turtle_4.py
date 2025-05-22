import turtle
import random
import time

# Configuração inicial
tela = turtle.Screen()
tela.title("Corrida das Tartarugas")
tela.setup(800, 400)

# Lista de cores para as tartarugas
cores = ["red", "blue", "green", "purple", "orange"]
tartarugas = []

# Criar e posicionar as 5 tartarugas
for i in range(5):
    t = turtle.Turtle(shape="turtle")
    t.color(cores[i])
    t.penup()
    t.setpos(-350, -100 + i * 50)  # Posiciona cada tartaruga em uma linha
    tartarugas.append(t)

# Linha de chegada
linha_chegada = 350
turtle.Turtle().penup()
turtle.Turtle().setpos(linha_chegada, -150)
turtle.Turtle().pendown()
turtle.Turtle().setpos(linha_chegada, 150)
turtle.Turtle().hideturtle()

# Solicitar palpite do usuário
palpite = tela.textinput("Escolha sua tartaruga", "Digite a cor (red, blue, green, purple, orange): ").lower()

# Função para mover as tartarugas
def mover_tartarugas():
    for t in tartarugas:
        velocidade = random.randint(1, 10)
        t.forward(velocidade)

# Ciclo de corrida
vencedora = None
while True:
    mover_tartarugas()
    for t in tartarugas:
        if t.xcor() >= linha_chegada:
            vencedora = t.pencolor()
            break
    if vencedora:
        break
    time.sleep(0.1)  # Pequena pausa para visualização

# Verificar o resultado
if palpite == vencedora:
    turtle.Turtle().write("Parabéns! Você acertou.", align="center", font=("Arial", 20, "bold"))
else:
    turtle.Turtle().write(f"Poxa vida! Você errou. Vencedora: {vencedora}", align="center", font=("Arial", 20, "bold"))

# Manter a janela aberta
tela.mainloop()