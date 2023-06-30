from tkinter import *
from tkinter import messagebox
root=Tk()


def msg():
    res = messagebox.askyesno("For Programmer", "Are you a programmer")

    if res == True:
        print("You are a programmer")
    else:
        print("You are not a programmer")


class objoriented2:



    def __init__(self):
        root.geometry("350x350")
        root.title("My new window")
        self.btn=Button(root,text="Testing",command=msg)
        self.btn.grid(row=1,column=1)


obj=objoriented2()
mainloop()