import turtle 

# Criando uma tartatura 
# Utilizando a função Turtle do módulo Turtle

tartaruga = turtle.Turtle()

#alterando o formato
tartaruga.shape("turtle")

#cor da tartaruga
tartaruga.color("medium aquamarine")

lado = 100

for i in range(4):
    tartaruga.forward(lado) #movimento
    #tartaruga.back(100) movimento de volta
    tartaruga.right(90) #rotação em graus de angulo, o left seria declarado da mesma forma


""" 
poderia ser feito dessa forma também
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.forward(100)
"""
turtle.done()