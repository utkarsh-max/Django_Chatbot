from tkinter import *

def printselecteditem():
    s=list.curselection()
    #print(s)
    for data in s:
        print(list.get(data))

def printdeleteditem():
    s = list.curselection()
    # print(s)
    for data in s:
        print(list.delete(data))

root=Tk()
frame=Frame(root)
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)
# in Browse mode you can use keyboard but in sngle mode y can not
list=Listbox(frame,width=15,selectmode=SINGLE,yscrollcommand=scroll.set)
'''list.insert(1,"Python")
list.insert(2,"Java")
'''
for i in range(20):
    print(i)
    list.insert(i,i+1)
list.pack()
scroll.config(command=list.yview)
frame.pack()

btn=Button(root,text="Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=printselecteditem)
btn.pack(side=BOTTOM,fill=X)

btn1=Button(root,text="Delete Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=printdeleteditem)
btn1.pack(side=BOTTOM,fill=X)

btn2=Button(root,text="CLOSE WINDOW",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=quit)
btn2.pack(side=BOTTOM,fill=X)
root.geometry("400x400+400+200")
#root.resizable(0,0)
mainloop()
