from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import *
root=Tk()

root.geometry("900x500")



lab=Label(root,text="Age Calculator",font=("Ariel",40,"bold"),bg="red",padx=500)
lab.grid(row=0,column=0,columnspan=10)


lab1=Label(root,text="Current Date")
lab1.grid(row=1,column=0)

today_date=datetime.now()
today_date_str=today_date.strftime('%d-%m-%Y')
currentv=StringVar(root,value=today_date_str)
entry=Entry(root,textvar=currentv,state=DISABLED)
entry.grid(row=1,column=2)

lab2=Label(root,text="Date Of Birth")
lab2.grid(row=2,column=0)



entry1=DateEntry(root,date_pattern="DD-MM-YYYY")
entry1.grid(row=2,column=2)

yearsentryv=IntVar()
monthsentryv=IntVar()
daysentryv=IntVar()


def calculation():
    current=currentv.get()
    dob=str(entry1.get())
    # current Date convert to integer
    global current_day,current_month,current_year
    current_day = int(current[0:2])
    current_month = int(current[3:5])
    current_year = int(current[6:10])

    # dob convert to integer
    global dob_day,dob_month,dob_year
    dob_day = int(dob[0:2])
    dob_month = int(dob[3:5])
    dob_year = int(dob[6:10])
    ############################################################
    lab = Label(root, text="Calculated Age", font=("Ariel", 40, "bold"), bg="green", padx=500)
    lab.grid(row=6, column=0, columnspan=10)
    lab1=Label(root,text="Years")
    lab1.grid(row=8,column=1)
    yearsentry=Entry(root,textvar=yearsentryv)
    yearsentry.grid(row=9,column=1)
    lab2 = Label(root, text="Months")
    lab2.grid(row=8, column=3)
    monthsentry = Entry(root,textvar=monthsentryv)
    monthsentry.grid(row=9, column=3)
    lab3 = Label(root, text="Days")
    lab3.grid(row=8, column=5)
    daysentry = Entry(root,textvar=daysentryv)
    daysentry.grid(row=9, column=5)

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dob_day > current_day:
        current_month = current_month - 1
        current_day=current_day+month[dob_month-1]

    if dob_month>current_month:
        current_year=current_year-1
        current_month=current_month+12

    ans_year=current_year-dob_year
    ans_month=current_month-dob_month
    ans_day=current_day-dob_day

    if ans_day<0 or ans_month<0 or ans_year<0:
        messagebox.showerror("Error In Selection","Please! Select Correct Date of Birth")
    else:
        yearsentryv.set(ans_year)
        monthsentryv.set(ans_month)
        daysentryv.set(ans_day)











btn=Button(root,text="Calculate Your Age",font=("Ariel",20,"italic"),command=calculation)
btn.grid(row=4,column=1)






















mainloop()