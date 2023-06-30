from tkinter import *


root=Tk()
root.title("Calculator")
frame=Frame(root,width=200,height=200)
i=StringVar()
radio=Radiobutton(frame,text="MALE",value="male",variable=i)
radio1=Radiobutton(frame,text="FEMALE",value="female",variable=i)
radio.pack()
radio1.pack()
btn=Button(frame,text="Click Me Top",fg="red",bg="yellow",
            font=("Ariel",12,'bold'))
btn.pack()
frame.pack(side=RIGHT)
j=IntVar()
frame1=Frame(root,width=200,height=200)
lblframe=LabelFrame(frame1,text="Select Your Caste")
lblframe.pack()
radio3=Radiobutton(lblframe,text="GENERAL",value="male",variable=j)
radio4=Radiobutton(lblframe,text="OBC",value="female",variable=j)
radio3.pack()
radio4.pack()

btn=Button(frame1,text="Click Me bottom",fg="red",bg="yellow",
            font=("Ariel",12,'bold'))
btn.pack()
frame1.pack(side=LEFT)

root.geometry("800x400+400+200")
#root.resizable(0,0)
mainloop()
