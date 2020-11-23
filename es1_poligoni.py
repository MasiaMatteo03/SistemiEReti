from turtle1 import Turtle
turtle = Turtle()
turtle.color("red")
turtle.begin_fill()
nLati = (int) (input("Numero di lati..."))
while True:
    turtle.forward(50)
    turtle.left(360 / nLati)
    if abs(turtle.pos()) <1:
        break
turtle.end_fill()
turtle.done()