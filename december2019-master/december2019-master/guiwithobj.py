from tkinter import *
from tkinter import messagebox

def msg():
    print("LEFT Click Me")
    s="10"
    #messagebox.showerror("Greeting","Good Day="+s)
    res=messagebox.askyesno("Question","Are U a Programmer?")
    print(res)
    if res==True:
        print("thank You")
    else:
        print("this is not for you")


class MyGui:

    def __init__(self,master):
        self.master=master
        self.btn=Button(master,text="Right Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=msg)
        self.btn.pack()

root=Tk()
ob=MyGui(root)

root.geometry("400x400+400+200")
root.resizable(0,0)
mainloop()
