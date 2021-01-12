from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3

top = Tk()
top.geometry("600x450+251+88")
top.minsize(120, 1)
top.maxsize(1284, 701)
top.resizable(1,  1)
top.title("Login")
    
def login():
    with sqlite3.connect('userinfo.db') as db:
        c = db.cursor()
    find_user = ('select * from Student signup where Email =? and Password =?')
    c.execute(find_user, [(e1.get()), (e2.get())])
    row = c.fetchone()
    if row==None:
        messagebox.showerror('Error', 'Please use an vaild username or password')
    else:
        messagebox.showinfo('Success', 'Welcome')
        top.destroy()
        import searchapp
    c.close

style = Style()
style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='black')

TLabel1 = ttk.Label(top)
TLabel1.place(relx=0.133, rely=0.311, height=19, width=55)
TLabel1.configure(text='''Gmail''')

e1 = ttk.Entry(top)
e1.place(relx=0.267, rely=0.311, relheight=0.047, relwidth=0.293)


TLabel2 = ttk.Label(top)
TLabel2.place(relx=0.133, rely=0.4, height=19, width=55)
TLabel2.configure(text='''Password''')

e2 = ttk.Entry(top)
e2.place(relx=0.267, rely=0.4, relheight=0.047, relwidth=0.293)
e2.configure(show="*")

t1 = Button(top,command=top.destroy)
t1.place(relx=0.3, rely=0.467, height=25, width=76)
t1.configure(text='cancel')

t2 = Button(top, command=login)
t2.place(relx=0.417, rely=0.467, height=25, width=76)
t2.configure(takefocus="")
t2.configure(text='''Login''')



top.mainloop()
