from turtle import *

t=Turtle()
window=Screen()

window.title("My Turtle")
t.shape("turtle")
t.color("green","yellow")
t.pensize(5)
t.speed(1)
t.hideturtle()
l=["red","blue","green","orange","grey"]
#t.circle(-50) #clockwise
#t.circle(100,steps=5)
t.pu()
t.goto(200,0)
t.pd()
#t.circle(100,extent=180)
for i in range(5):
    t.color(l[i])
    t.circle(50)
    t.pu()
    t.backward(100)
    t.pd()
done()