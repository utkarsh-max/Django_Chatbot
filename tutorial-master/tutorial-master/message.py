from tkinter import *
from tkinter import messagebox
root=Tk()

def messagebox1():
    messagebox.showinfo("Message","Operation Successfull Here Your Message Box")
    

btn_Label=Label(root,text="Click To Display Message Box")
btn_Label.grid(row=0,column=0)

btn=Button(root,text="Message Box Button",command=messagebox1)
btn.grid(row=0,column=1)
















mainloop()
