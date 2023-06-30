#----------------Import Turtle Module--------
from turtle import *
#------------Creating Turtle Object-------
t = Turtle()
#------------Control Turtle Speed--------
t.speed(0)
#------------ Control Various Attributes of Screen Window-------
wn = Screen()
wn.bgcolor("Cyan")
title("Design2")
#----------Main Logic----------
for i in range(180):
    t.forward(150)
    t.right(30)
    t.forward(30)
    t.left(60)
    t.forward(70)
    t.right(30)
    t.penup()
    t.setposition(0 , 0)
    t.pendown()
    t.right(2)
#-------Turtle Termination---------
done()
