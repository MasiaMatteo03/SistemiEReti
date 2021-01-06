import turtle
bob = turtle.Turtle()
win = turtle.Screen()
width = 1000
height = 1000
angle = 90
step = 100



bob.begin_fill()
win.bgcolor("yellow")

def up():
    print(bob.pos())
    if(bob.ycor()+step >= height//2 or bob.xcor()+step >= width//2 or bob.ycor()+step <= -height//2 or bob.xcor()+step <= -width//2):
        bob.forward(step)

def down():
    print(bob.pos())
    
    if(bob.ycor()-step >= height//2 or bob.xcor()-step >= width//2 or bob.ycor()-step <= -height//2 or bob.xcor()-step <= -width//2):
        bob.backward(step)

def left():
    bob.left(angle)
    
def right():
    bob.right(angle)
    
def main():
    win.setup(width = width, height = height)
    
    win.onkey(up, "w")
    win.onkey(down, "s")
    win.onkey(left, "a")
    win.onkey(right, "d")
    win.listen()
    win.mainloop()

if __name__ == "__main__":
    main()