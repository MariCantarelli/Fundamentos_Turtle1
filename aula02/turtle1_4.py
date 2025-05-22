import turtle

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("#ff0000")
tartaruga.pencolor("#00ff00") #cor da linha

for step in range(0, 4):
    tartaruga.forward(100)
    tartaruga.left(90) 