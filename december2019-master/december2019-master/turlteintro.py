from turtle import *
#help('turtle.shape')
'''
Shape with name must exist in the TurtleScreen's shape dictionary.
    Initially there are the following polygon shapes:
    'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
help('turtle.penup')
help('turtle.pendown')
'''
t=Turtle()
window=Screen()
#window.bgcolor("yellow")
#window.bgcolor('170','70','10')
#window.bgpic("test.gif")
window.title("My Turtle")
t.shape("turtle")
t.color("green","yellow")
t.pensize(5)
t.speed(1)
t.hideturtle()
t.begin_fill()
t.goto(10,50)
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()


t.penup()
t.forward(100)
t.pendown()
t.color("blue","gold")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.undo()
t.clear()
#t.reset()
'''
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.forward(100)
t.end_fill()
'''
'''
t.penup()
t.forward(200)
t.pendown()
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
done()