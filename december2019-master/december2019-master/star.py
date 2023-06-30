from turtle import *

t=Turtle()
window=Screen()

window.title("My Turtle")
t.shape("turtle")
t.color("green","yellow")
t.pensize(5)
t.hideturtle()
l=["red","blue","green","orange","grey"]
for i in range(5):
    t.color(l[i])
    t.forward(300)
    t.left(144)

done()