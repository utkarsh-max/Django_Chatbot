from tkinter import *
from PIL import Image,ImageTk

def msg():
    print("hi")

root=Tk()
root.wm_iconbitmap("note.ico")   #to add icon

mainMenu=Menu(root)
root.config(menu=mainMenu)

fileMenu=Menu(mainMenu,tearoff=False)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=msg,accelerator="Ctrl+N")
fileMenu.add_separator()
fileMenu.add_command(label="open",command=msg)


editMenu=Menu(mainMenu)
mainMenu.add_cascade(labe="Edit",menu=editMenu)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()

