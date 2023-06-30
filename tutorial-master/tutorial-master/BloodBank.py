from tkinter import *

root=Tk()
window_height=root.winfo_screenheight()
window_width=root.winfo_screenwidth()
root.geometry("%dx%d"%(window_width,window_height))
def mainheading():
    label=Label(root,text="Blood Bank Login Window",font=('Ariel',30,'bold'),padx=450,bg="green")
    label.grid(row=0,column=0)
mainheading()
mainloop()