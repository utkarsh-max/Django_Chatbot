from tkinter import *

def msg(event=''):
    print("LEFT Click Me")


def msg1(event):
    print("Middle Click Me")

def msg2(event):
    print("Right Click Me")

root=Tk()
root.title("Calculator")
root.bind("<Control-t>",msg)



btn=Button(root,text="LEFT Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=msg)
#btn.bind("<Button-1>",msg)
btn.pack(side=TOP,fill=X)

btn1=Button(root,text="Middle Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'))
btn1.bind("<Button-2>",msg1)
btn1.pack()


btn2=Button(root,text="Right Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'))
btn2.bind("<Button-3>",msg2)
btn2.pack(side=BOTTOM,fill=X)
'''
side=LEFT,RIGHT,TOP,BOTTOM
'''
#label.place(x=40,y=60)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()
