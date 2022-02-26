import sqlite3
import os,sys
import win32print
import win32api
import tempfile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Billing")
root.geometry("1366x768")
root.config(bg="aqua")
root.iconbitmap("tech.ico")

#bill_no = IntVar()
c_name = StringVar()
phone = StringVar()
product_name = StringVar()
Quantity = IntVar()
Rate = IntVar()



global l
l = []

global count
count = 0

title=Label(root,text="Siva Textile",bg="dodgerblue",fg="black",font=("Times New Roman",20,"bold"),relief=GROOVE,bd=8)
title.pack(fill=X)


F1 = Frame(root,bg="dodgerblue",relief=RAISED,bd=15)
F1.place(x=10,y=60,width=650,height=530)

lb1 = Label(F1,text="Customer Name",width="15",fg="black",bg="dodgerblue",font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
lb1.grid(row=0,column=0,padx=30,pady=10,sticky="w")
ent1 = Entry(F1,fg="black",bg="dodgerblue",textvariable=c_name,font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
ent1.grid(row=0,column=1,padx=30,pady=10,sticky="w")

lb2 = Label(F1,text="Phone Number",width="15",fg="black",bg="dodgerblue",font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
lb2.grid(row=1,column=0,padx=30,pady=10,sticky="w")
ent2 = Entry(F1,fg="black",bg="dodgerblue",textvariable=phone,font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
ent2.grid(row=1,column=1,padx=30,pady=10,sticky="w")

lb3 = Label(F1,text="Product Name",width="15",fg="black",bg="dodgerblue",font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
lb3.grid(row=2,column=0,padx=30,pady=10,sticky="w")
ent3 = Entry(F1,fg="black",bg="dodgerblue",textvariable=product_name,font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
ent3.grid(row=2,column=1,padx=30,pady=10,sticky="w")

lb4 = Label(F1,text="Product Quantity",width="15",fg="black",bg="dodgerblue",font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
lb4.grid(row=3,column=0,padx=30,pady=10,sticky="w")
ent4 = Entry(F1,fg="black",bg="dodgerblue",textvariable=Quantity,font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
ent4.grid(row=3,column=1,padx=30,pady=10,sticky="w")

lb5 = Label(F1,text="Product Rate",width="15",fg="black",bg="dodgerblue",font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
lb5.grid(row=4,column=0,padx=30,pady=10,sticky="w")
ent5 = Entry(F1,fg="black",bg="dodgerblue",textvariable=Rate,font=("Times New Roman",15,"bold"),relief=RIDGE,bd=8)
ent5.grid(row=4,column=1,padx=30,pady=10,sticky="w")

con = sqlite3.connect("siva.db")
cur = con.cursor()
con.commit()
con.close()

#####################################################################################

def welcome():

    textarea.delete(1.0,END)
    textarea.insert(END,"\t Welcome Siva Textile")
    textarea.insert(END, f'\nCustomer Name  :\t\t{c_name.get()}')
    textarea.insert(END, f'\nPhone Number   :\t\t{phone.get()}')
    textarea.insert(END,f"\n---------------------------------------------------------------------")
    textarea.insert(END,f'\n Product\t\tQTY\t\tPrice')
    textarea.insert(END,f"\n---------------------------------------------------------------------")
    textarea.config(font="Times 15 bold")

#####################################################################################


def add():
    m = Quantity.get()*Rate.get()
    l.append(m)

    if c_name == '':
        messagebox.showerror("Error","Please enter any product")
    elif product_name == '':
        messagebox.showerror("Error","Please enter any product")
    else:
        textarea.insert(END,f'\n{product_name.get()}\t\t{Quantity.get()}\t\t{m}')



#####################################################################################
def gbill():
    n = Rate.get()
    m = Quantity.get() * n
    l.append(m-m)
    tex = textarea.get(7.0,(7.0+float(len(l))))
    welcome()
    textarea.insert(END,tex)
    textarea.insert(END,f"\n---------------------------------------------------------------------")
    textarea.insert(END,f"\nTotal Paybill Amount : \t\t\t\t{sum(l)}")
    textarea.insert(END,f"\n---------------------------------------------------------------------")

def save():
    a = c_name.get()
    b = phone.get()
    n = Rate.get()
    m = Quantity.get() * n
    l.append(m - m)
    c = sum(l)
    con = sqlite3.connect("siva.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customer (
                    CustomerName TEXT,
                    Phone TEXT,
                    price INTEGER
                    )""")
    cur.execute("""INSERT INTO customer (CustomerName,Phone,price) VALUES(?,?,?)""",(a,b,c,))
    messagebox.showinfo("Data are Inserted","successfully")
    con.commit()


#####################################################################################
def clear():
    textarea.delete(1.0,END)
    c_name.set("")
    phone.set("")
    product_name.set("")
    Quantity.set("")
    Rate.set("")
    welcome()

def print():
    q = textarea.get("1.0","end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(q)
    os.startfile(filename,"print")
#####################################################################################

def exit():
    op = messagebox.askyesno("Exit","Do you really want to Exit")
    if op>0:
        root.destroy()
        return
#####################################################################################

def see():
    boot = Tk()
    boot.title("Billing")
    boot.geometry("1366x768")
    boot.config(bg="grey")
    boot.iconbitmap("tech.ico")

    style = ttk.Style()
    style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="silver")
    style.map("Treeview",background=[('selected','green')])

    my_tree = ttk.Treeview(boot,height=500)
    my_tree['columns']=['CusotmerName','PhoneNumber','Rate']
    my_tree.column("CusotmerName",width=400)
    my_tree.column("PhoneNumber",width=400)
    my_tree.column("Rate",width=400)

    my_tree.heading("CusotmerName", text="Customer name",anchor=W)
    my_tree.heading("PhoneNumber",text="Phone number",anchor=W)
    my_tree.heading("Rate",text="Rate",anchor=W)
    my_tree.pack()

    con = sqlite3.connect("siva.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM customer")
    record = cur.fetchall()
    for i in record:
        my_tree.insert(parent='',index="end",values=(i[0],i[1],i[2]))
    con.commit()
    con.close()

    boot.mainloop()

#####################################################################################


btn1 = Button(F1,text="Add",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=add)
btn1.grid(row=7,columnspan=2,padx=20,pady=10)

F2 = Frame(root,bg="dodgerblue",relief=SUNKEN,bd=15)
F2.place(x=730,y=60,width=610,height=530)

bill_title = Label(F2,text="Billing Area",relief=RAISED,bd="7",bg="aqua",fg="black",font=("Times 15 bold"))
bill_title.pack(fill=X)

#scroll with textareabox
scrol = Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea = Text(F2,font=("Times New Roman",15,"bold"),fg="black",yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview())
welcome()
F3 = Frame(root,bg="dodgerblue",relief=SUNKEN,bd=15)
F3.place(x=10,y=600,width=1340,height=100)

btn2 = Button(F3,text="Print",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=print)
btn2.grid(row=0,column=1,padx=20,pady=10)

btn3 = Button(F3,text="Reset",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=clear)
btn3.grid(row=0,column=2,padx=20,pady=10)

btn4 = Button(F3,text="Generate Bill",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=gbill)
btn4.grid(row=0,column=3,padx=20,pady=10)

btn5 = Button(F3,text="Exit",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=exit)
btn5.grid(row=0,column=4,padx=20,pady=10)

btn6 = Button(F3,text="Save",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=save)
btn6.grid(row=0,column=5,padx=20,pady=10)

btn7 = Button(F3,text="see Data",font=("Times New Roman",15,"bold"),fg="black",bg="lightsteelblue",command=see)
btn7.grid(row=0,column=6,padx=20,pady=10)

#this function for to go tree view
welcome()
root.mainloop()