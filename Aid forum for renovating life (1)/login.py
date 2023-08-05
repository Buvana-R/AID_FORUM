from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
def log():
    number = phone_number.get()
    password = pass_word.get()

    sql = "SELECT * FROM users WHERE number=%s AND password=%s"
    val = (number, password)
    cur.execute(sql, val)
    result = cur.fetchone()
    con.commit()
    if result:
        messagebox.showinfo("Info","Login successfully")
    else:
        messagebox.showinfo("Info","Invalid phonenumber or password")

    phone_number.delete(0, END)
    pass_word.delete(0, END)
    root.destroy()


def login():
    global phone_number,pass_word,Canvas1,userTable,con,cur
    root = Tk()
    root.title("Login")
    root.geometry("400x300")

    mypass = "Suthan"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    userTable="users"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="PhoneNumber", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    phone_number = Entry(labelFrame)
    phone_number.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
    lb2 = Label(labelFrame,text="Password", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    pass_word = Entry(labelFrame,show="*")
    pass_word.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    
    SubmitBtn = Button(root,text="Login",bg='#d1ccc0', fg='black',command=log)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
