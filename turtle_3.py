import turtle 

def desenhar (x, y, w, h, cor):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(cor)
    for i in range(2):
        t.fd(w)
        t.left(90)
        t.fd(h)
        t.left(90)
    t.end_fill()
        

t = turtle.Turtle()
desenhar(0, 0, 50, 50, "#FF8200")
##desenhar(0, 0, 100, 50, "#FFC000")


