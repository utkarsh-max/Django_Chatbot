from turtle import *
from random import *
t = Turtle()
speed(0)
colormode(255)
bgcolor("Black")
print(window_width())
setup(1920,720,0,0)
def draw_square():
    for side in range(4):
        forward(160)
        right(90)
        for side in range(4):
            forward(80)
            right(90)
penup()
back(40)
pendown()
for square in range(75):
    color1 = randrange(1,255)
    color2 = randrange(1, 255)
    color3 = randrange(1, 255)
    l = (color3,color2,color1)
    pencolor(l)
    speed(0)
    draw_square()
    forward(5)
    left(5)
done()