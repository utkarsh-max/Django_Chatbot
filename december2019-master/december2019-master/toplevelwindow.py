from tkinter import *
from PIL import Image,ImageTk

def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha()or P == " ":  # if a digit was entered or nothing was entered
        return True
    return False

root=Tk()
root.wm_iconbitmap("note.ico")   #to add icon
path="login.png"
img = ImageTk.PhotoImage(Image.open(path))
def opennewwindow():
    top=Toplevel()
    top.title("NEW window")
    btn2 = Button(top, text="CLOSE WINDOW", fg="red", bg="yellow",
                  font=("Ariel", 12, 'bold'), command=top.destroy)
    btn2.pack(side=BOTTOM, fill=X)
    top.geometry("400x400+400+200")

my_entry = Entry(root)  # creates an entry
my_entry.pack()  # shows it in the root window using grid geometry manager

my_entry1 = Entry(root)  # creates an entry
my_entry1.pack()

callback = root.register(only_char_input)  # registers a Tcl to Python callback
callback1 = root.register(only_numeric_input)  # registers a Tcl to Python callback

my_entry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation
my_entry1.configure(validate="key", validatecommand=(callback1, "%P"))
btn2=Button(root,text="CLOSE WINDOW",image=img,fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=opennewwindow)
btn2.pack(side=BOTTOM,fill=X)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()


'''
# valid percent substitutions (from the Tk entry main page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget




'''