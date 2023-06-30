

class Add:

    def __init__(self):
        a,b=10,20
        print(a+b)









obj=Add()

from tkinter import *
from tkinter import simpledialog

root=Tk()

def test():
    try:
        a=simpledialog.askinteger("Number Dialog","Please Enter a Number")
        b = simpledialog.askinteger("Number Dialog", "Please Enter again a Number")
        print(a+b)

    except Exception:
        print("Please Enter a Valid Number and Click OK for both dialog box")

btn=Button(root,text="Test",command=test)
btn.grid(row=0,column=0)






mainloop()
