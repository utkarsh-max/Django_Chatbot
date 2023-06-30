from tkinter import *
from tkinter import filedialog,colorchooser

def colorchoose():
    col=colorchooser.askcolor(title="Select your color")
    print(col)
    root.configure(background=col[1])
def getdata():
    s=my_entry1.get(1.0,END)
    print(s)

def selectedgetdata():
    res=my_entry1.selection_get()
    print(res)

def selectedposition():
    res=my_entry1.selection_get()
    pos=my_entry1.search(res,1.0,stopindex=END)
    print(pos)

def clear():
    my_entry1.delete(1.0,END)

def openfile():
    result=filedialog.askopenfile(initialdir="/",title="Select To openfile",
                                  filetypes=(("Text FILE","*.txt"),("ALL FILE","*.*")))
    # to print the text of file
    for data in result:
        print(data)
        my_entry1.insert(INSERT, data)
    print(result)
root=Tk()
#root.wm_iconbitmap("note.ico")   #to add icon

my_entry1 = Text(root,selectbackground='green',wrap=WORD,insertwidth=1)  # creates an entry
my_entry1.insert(INSERT,"Hello how r U?")
my_entry1.pack()

btn2 = Button(root, text="print text", fg="red", bg="yellow",
              font=("Ariel", 12, 'bold'), command=getdata)
btn2.pack(side=BOTTOM, fill=X)
btn3 = Button(root, text="print selected text", fg="red", bg="yellow",
              font=("Ariel", 12, 'bold'), command=selectedgetdata)
btn3.pack(side=BOTTOM, fill=X)

btn4 = Button(root, text="print selected text position", fg="red", bg="yellow",
              font=("Ariel", 12, 'bold'), command=selectedposition)
btn4.pack(side=BOTTOM, fill=X)

btn5 = Button(root, text="clear text ", fg="red", bg="yellow",
              font=("Ariel", 12, 'bold'), command=clear)
btn5.pack(side=BOTTOM, fill=X)
btn6 = Button(root, text="openfile ", fg="red", bg="yellow",
              font=("Ariel", 12, 'bold'), command=openfile)
btn6.pack(side=BOTTOM, fill=X)

btn7 = Button(root, text="Color Chooser ", fg="red", bg="yellow",
              font=("Ariel", 12, 'bold'), command=colorchoose)
btn7.pack(side=BOTTOM, fill=X)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()


