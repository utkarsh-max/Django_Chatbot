import tkinter
from tkinter import ttk

def clear_fields():
    qty_entry.delete(0, tkinter.END)
    qty_entry.insert(0, "1")
    description_entry.delete(0, tkinter.END)
    unit_price_entry.delete(0, tkinter.END)
    unit_price_entry.insert(0, "1")


def add_item():
    qty = int(qty_entry.get())
    desc = description_entry.get()
    unit_price = int(unit_price_entry.get())
    total = qty*unit_price
    ls_invoice = [qty,desc,unit_price,total]
    tree.insert('', 0, values=ls_invoice)
    clear_fields()
    qty_entry.focus_set()
    # print(qty," ",desc," ",unit_price)

def new_invoice():
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    tree.delete(*tree.get_children())
    clear_fields()
    first_name_entry.focus_set()

window = tkinter.Tk()

window.title("Invoice Generator Software")

frame = tkinter.Frame(window)
frame.pack(padx=30, pady=10)

first_name_lable = tkinter.Label(frame, text="First Name")
first_name_lable.grid(row=0, column=0, pady=10)

first_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=1, column=0, pady=10)

last_name_lable = tkinter.Label(frame, text="Last Name")
last_name_lable.grid(row=0, column=1, pady=10)

last_name_entry = tkinter.Entry(frame)
last_name_entry.grid(row=1, column=1, pady=10)

phone_lable = tkinter.Label(frame, text="Phone")
phone_lable.grid(row=0, column=2, pady=10)

phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1, column=2, pady=10)

qty_lable = tkinter.Label(frame, text="Qty")
qty_lable.grid(row=2, column=0, pady=10)

qty_entry = tkinter.Spinbox(frame, from_=1, to=100)
qty_entry.grid(row=3, column=0, pady=10)

description_lable = tkinter.Label(frame, text="Discription")
description_lable.grid(row=2, column=1, pady=10)

description_entry = tkinter.Entry(frame)
description_entry.grid(row=3, column=1, pady=10)

unit_price_lable = tkinter.Label(frame, text="Unit Price")
unit_price_lable.grid(row=2, column=2, pady=10)

unit_price_entry = tkinter.Spinbox(frame, from_=1, to=100)
unit_price_entry.grid(row=3, column=2, pady=10)

add_item_button = tkinter.Button(frame, text="Add Item", command=add_item)
add_item_button.grid(row=4, column=2, pady=10)

columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Price')
tree.heading('total', text='Total')
tree.grid(row=5, column=0, columnspan=3, pady=10)

gen_invoice_button = tkinter.Button(frame, text="Generate Invoice")
gen_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", pady=10)

new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", pady=10)
window.mainloop()
