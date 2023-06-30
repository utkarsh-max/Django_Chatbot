from tkinter import *
from tkinter import messagebox,ttk,filedialog
from tkinter import ttk
import pymysql
from  datetime import datetime
taz=Tk()
########### main treeview #################
tazTV = ttk.Treeview(height=10, columns=('Item Name''Rate','Type'))
############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False
callback = taz.register(only_char_input)  # registers a Tcl to Python callback
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback
############# bill generation ########################
def billgenerationwindow():
    pass
#############################
############## back buttton #####################

def backbutton():
    remove_all_widgets()
    mainheading()
    welcomewindow()
########## add item ################

def additem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemTypeVar.get()
    print(name, rate, type)
    dbconfig()
    query = "insert into itemlist (item_name,item_rate,item_type) values(%s,%s,%s);"
    val = (name, rate, type)
    mycursor.execute(query, val)
    conn.commit()
    messagebox.showinfo("Save Data", 'Item Inserted Successfully')
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    # to fetch data in treeview
    getItemInTreeView()
############ get Item in tree view ###############
def getItemInTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    print(mycursor)
    query = "select * from itemlist"
    mycursor.execute(query)
    data = mycursor.fetchall()
    print(data)

    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"], row["item_type"]))

    conn.close()
#######################################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()

def additemwindow():
    remove_all_widgets()
    mainheading()
    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=1, column=3, columnspan=1)

    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=5, pady=5)
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=5, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=5, pady=5)
    itemTypeEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=additem)
    additemButton.grid(row=5, column=2, columnspan=1)

    label = Label(taz)
    label.grid(row=6, column=2, padx=20, pady=5)
    ###############################################
    tazTV.grid(row=7, column=0, columnspan=3)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview", fieldbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=2, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")
    # to fetch data in treeview
    getItemInTreeView()
#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
############ mainheading creation ###########
def mainheading():
    label = Label(taz, text="Hotel WahTaz Management system", bg="yellow", fg="green",
                  font=("Comic Sans Ms", 40, "bold"), padx=0, pady=0)
    label.grid(row=0, columnspan=4)
##############################################
############# def logout ########################
def logout():
    remove_all_widgets()
    mainheading()
    loginwindow()
############### database conncetion #########################
def dbconfig():
    global mycursor,conn
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor()

############ Welcome window ############
def welcomewindow():
    remove_all_widgets()
    mainheading()
    welcomeLabel = Label(taz, text="Welcome User", font="Arial 30")
    welcomeLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    additemButton = Button(taz, text="Manage Restaurant", width=20, height=2, fg="green", bd=10, command=additemwindow)
    additemButton.grid(row=3, column=0, columnspan=1)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10,
                        command=billgenerationwindow)
    billButton.grid(row=3, column=1, columnspan=2)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=3, columnspan=1)


############### admin Login ###################
def adminlogin():
    username = usernameVar.get()
    password = passwordVar.get()
    if(username=="" or password==""):
        messagebox.showerror("Data Filling Error","Please Fill user Name and Password both")
    else:
        dbconfig()
        que = "select * from user_info where userid=%s and password=%s"
        val = (username, password)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        conn.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            usernameVar.set("")
            passwordVar.set("")

##########################################
############### login window ####################
usernameVar = StringVar()
passwordVar = StringVar()

def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)
    usernameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)


################################################
screen_width=taz.winfo_screenwidth()
#print(screen_width)
screen_height=taz.winfo_screenheight()
#print(screen_height)
taz.title("Hotel WAhTaz Managment System")
mainheading()
loginwindow()

#taz.geometry("900x600+120+50")
taz.geometry("%dx%d+0+0"%(screen_width,screen_height))
mainloop()