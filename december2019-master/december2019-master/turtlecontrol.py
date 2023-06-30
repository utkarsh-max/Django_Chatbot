#import turtle
from turtle import *
s=Turtle()
sc=Screen()
def up():
    s.forward(100)
def down():
    s.backward(100)
def right():
    s.right(90)
    s.forward(100)
def left():
    s.left(90)
sc.onkey(up,"D")
#sc.onkey(up,"space")
sc.onkey(down,"Down")
sc.onkey(right,"Right")

sc.onkey(left,"Left")
sc.listen()
done()

