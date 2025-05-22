import turtle

def desenhar_pixel_art(matriz, pos_x, pos_y, cores, tamanho_pixel):
    altura = len(matriz)
    largura = len(matriz[0]) if altura > 0 else 0

    turtle.speed(0)  # Desenha rapidamente
    turtle.penup()
    turtle.hideturtle()

    for linha in range(altura):
        for coluna in range(largura):
            cor_index = matriz[linha][coluna]
            if 0 <= cor_index < len(cores):
                turtle.goto(pos_x + coluna * tamanho_pixel, pos_y - linha * tamanho_pixel)
                turtle.fillcolor(cores[cor_index])
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(tamanho_pixel)
                    turtle.right(90)
                turtle.end_fill()

# Exemplo de matriz usando as cores 0 a 3
matriz_exemplo = [
    [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,1,1,0,0,2,2,0,0,1,1,0,0,0],
    [0,0,1,0,0,0,2,2,2,2,0,0,0,1,0,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],
    [1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],
    [1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],
    [1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,1],
    [0,1,1,1,3,3,1,3,3,1,3,3,1,1,1,0],
    [0,0,1,3,3,3,1,3,3,1,3,3,3,1,0,0],
    [0,0,1,3,3,3,3,3,3,3,3,3,3,1,0,0],
    [0,0,0,1,3,3,3,3,3,3,3,3,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]
]


# Paleta de cores fornecida
cores = [
    "#ffffff",  # 0 - branco
    "#000000",  # 1 - preto
    "#F80500",  # 2 - vermelho
    "#F7C192"   # 3 - pele
]

# Parâmetros de desenho
pos_x = -100
pos_y = 100
tamanho_pixel = 20

# Desenhar
desenhar_pixel_art(matriz_exemplo, pos_x, pos_y, cores, tamanho_pixel)

turtle.done()
