import turtle
bob = turtle.Turtle()
win = turtle.Screen()

bob.begin_fill()
win.bgcolor("yellow")

def up():
    print(bob.pos())
    bob.forward(50)
    if(bob.ycor() >= 500 or bob.xcor() >= 500 or bob.ycor() <= -500 or bob.xcor() <= -500):
        bob.reset()

def down():
    print(bob.pos())
    bob.backward(50)
    if(bob.ycor() >= 500 or bob.xcor() >= 500 or bob.ycor() <= -500 or bob.xcor() <= -500):
        bob.reset()

def left():
    bob.left(90)
    

def right():
    bob.right(90)
    

win.setup(width=1000, height=1000)
win.listen()
win.onkey(up, "Up")
win.onkey(down, "Down")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.mainloop()