from tkinter import *

root=Tk()


def newwindow():
    new=Toplevel()
    new.title("New Window")
    lbl=Label(new,text="Ststus Bar")
    lbl.grid(sticky="nsew")
    lbl.grid_rowconfigure(row=15,weight=1,column=1)

btn=Button(root,text="New Window",command=newwindow)
btn.grid(row=0,column=0)












mainloop()