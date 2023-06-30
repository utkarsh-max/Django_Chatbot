from tkinter import *
from tkinter import simpledialog

def getRadioValue():
    print(i.get())
    print(j.get())

def getname():
    s=simpledialog.askstring("Input box","Please enter your name")
    print(s)
root=Tk()
root.title("Calculator")
i=IntVar()
radio=Radiobutton(root,text="MALE",value=1,variable=i,indicatoron=0)
radio1=Radiobutton(root,text="FEMALE",value=2,variable=i)
radio.pack()
radio1.pack()

k=IntVar()
j=IntVar()
check1=Checkbutton(root,text="Hindi",variable=k)
check2=Checkbutton(root,text="English",variable=j)
check1.pack()
check2.pack()


btn=Button(root,text="Click Me bottom",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=getRadioValue)
btn.pack()

btn=Button(root,text="Click Me Input your name",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=getname)
btn.pack()
root.geometry("800x400+400+200")
#root.resizable(0,0)
mainloop()
