from tkinter import *

def msg():
    print("hi")
    s=x.get()
    print(s)
    x.set("")
    print(y.get())
    out.set(s)
root=Tk()
root.title("Calculator")
label=Label(root,text="Enter your Name",fg="red",bg="yellow",
            font=("Ariel",12,'bold'))
label.pack()

#text=Entry(root,font=("Ariel",25,'bold'),show="*")
x=StringVar()
text=Entry(root,font=("Ariel",25,'bold'),textvariable=x)

y=IntVar()
text1=Entry(root,font=("Ariel",25,'bold'),textvariable=y)

out=StringVar()
textout=Entry(root,font=("Ariel",25,'bold'),textvariable=out)
#text.set("hello")
text.pack()
text1.pack()
textout.pack()
btn=Button(root,text="Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=msg)
btn.pack(side=BOTTOM,fill=X)

'''
side=LEFT,RIGHT,TOP,BOTTOM
'''
#label.place(x=40,y=60)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()
