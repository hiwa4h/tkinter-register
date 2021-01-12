from tkinter.ttk import *
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('Register-Form')
root.geometry("600x450+-2+86")
root.minsize(120, 1)

def delete():
    if(Entry1.get()==''):
        messagebox.showerror('Register-Form', 'ID Is compolsary for delete')
    else:
        ms = messagebox.askokcancel('Delete Result', 'Would you like to delete this account?')
        if (ms):
            conn = sqlite3.connect('userinfo.db')
            with conn:
                c = conn.cursor()
            c.execute("delete from student where id='"+ Entry1.get() +"'")
            c.execute('commit')
            Entry1.delete(0, END)
            Entry2.delete(0, END)
            Entry3.delete(0, END)
            Entry4.delete(0, END)
            messagebox.showwarning('Delete Status', 'Deleted Succesfully')
            conn.close()

def sign_in():
        root.destroy()
        import main

def insert_info():
    idp=Entry1.get()
    un=Entry2.get()
    password=Entry3.get()
    if (idp=='' and password=='' and un==''):
        messagebox.showerror('Submit Status', 'All fields are requierd')
    elif Entry3.get() != Entry4.get():
            messagebox.showerror('register error', 'please confirm password')
            Entry4.delete(0, END) 
            Entry4.focus()
    else:
        try:
            id1=Entry1.get();
            uname=Entry2.get();
            password1=Entry3.get();

            conn = sqlite3.connect('userinfo.db')
            with conn:
                c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS Student (ID INTEGER, Email TEXT, Password1 TEXT, Password2 TEXT)")
            c.execute("INSERT INTO Student (ID,Email,Password) VALUES(?,?,?)", (id1, uname, password1))
            conn.commit()
            conn.close()
            messagebox.showinfo('Register Form', 'Account Created Successfully!')
            Entry1.delete(0, END)
            Entry2.delete(0, END)
            Entry3.delete(0, END)
            Entry4.delete(0, END)
        except  sqlite3.IntegrityError:
            messagebox.showerror('Register Form', f'Please use another id instead of {Entry1.get()} because that id exists')
            Entry1.focus()

Label1 = ttk.Label(root)
Label1.place(relx=0.35, rely=0.156, height=21, width=44)
Label1.configure(text='''Enter ID:''')

Label2 = ttk.Label(root)
Label2.place(relx=0.35, rely=0.2, height=31, width=54)
Label2.configure(text='''UName:''')

Label3 = ttk.Label(root)
Label3.place(relx=0.333, rely=0.289, height=21, width=64)
Label3.configure(text='''Password:''')

Label4 = ttk.Label(root)
Label4.place(relx=0.267, rely=0.356, height=21, width=104)
Label4.configure(text='''Confirm Password:''')

Entry1 = ttk.Entry(root)
Entry1.place(relx=0.45, rely=0.156, height=20, relwidth=0.273)

Entry2 = ttk.Entry(root)
Entry2.place(relx=0.45, rely=0.222, height=20, relwidth=0.273)

Entry3 = ttk.Entry(root, show='*')
Entry3.place(relx=0.45, rely=0.289, height=20, relwidth=0.273)


Entry4 = ttk.Entry(root, show='*')
Entry4.place(relx=0.45, rely=0.356, height=20, relwidth=0.273)

b0 = ttk.Button(root, command=sign_in)
b0.place(relx=0.467, rely=0.578, height=84, width=87)
b0.configure(text='Sign in')


b1 = ttk.Button(root, text='Submit', command=insert_info)
b1.place(relx=0.767, rely=0.578, height=84, width=87)


B3 = ttk.Button(root, command=delete)
B3.place(relx=0.617, rely=0.578, height=84, width=87)
B3.configure(text='''Delete''')



root.mainloop()
