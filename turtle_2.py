import turtle 

tartaruga = turtle.Turtle()

lado = 100

for i in range(3):
    tartaruga.forward(lado)
    tartaruga.left(120) #usamos 120 pois seria oq falta para 180 graus
    
"""
ou poderia ser feito dessa forma 
tartaruga.forward(100)
tartaruga.left(120)
tartaruga.forward(100)
tartaruga.left(120)
tartaruga.forward(100)
    
"""

turtle.done()