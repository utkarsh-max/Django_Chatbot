from tkinter import *
from tkinter.ttk import Combobox

def getdata():
    v=combo.get()
    print(v)
    print(s.get())
    print(spin.get())
root=Tk()
#country=["India","china","PaKistan"]
country=list(range(1,230))
combo=Combobox(root,value=country)
combo.set("Select Your country")
combo.pack()

s=Scale(root,from_=50,to=150,orient=HORIZONTAL,length=250,width=20,sliderlength=100)
s.set(100)
s.pack()

spin=Spinbox(root,from_=1,to=5)
spin.pack()


btn2=Button(root,text="Print Combo Value",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=getdata)

btn2.pack(side=BOTTOM,fill=X)
'''
side=LEFT,RIGHT,TOP,BOTTOM
'''
#label.place(x=40,y=60)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()
