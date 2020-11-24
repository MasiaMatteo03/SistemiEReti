from turtle1 import Turtle
prova = Turtle()
prova.color('red', 'yellow')
prova.begin_fill()
while True:
    prova.forward(200)
    prova.left(170)
    if abs(prova.pos()) < 1:
        break
prova.end_fill()
prova.done()