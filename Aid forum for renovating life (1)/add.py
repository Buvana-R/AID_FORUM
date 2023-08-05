from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def add():
    
    name=person_name.get()
    phone_number=contact_number.get()
    location=locat_ion.get()
    
    sql = "INSERT INTO contacts (name, phone_number, location) VALUES (%s, %s, %s)"
    val=(name,phone_number,location)
    cur.execute(sql,val)
    try:
        con.commit()
        s="select address,phno from location where location= %s"
        v=location
        cur.execute(s,v)
        query_result = cur.fetchall()
        con.commit()
        result_string = ""
        for row in query_result:
            result_string += str(row) + "\n"
        messagebox.showinfo(title='Success',message=result_string)
    except:
        messagebox.showerror("Error", "An error has occurred.")
    
    

    root.destroy()
    
def addProduct(): 
    
    global person_name,contact_number,locat_ion,Canvas1,con,cur,contactTable,root
    
    root = Tk()
    root.title("Add")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Suthan"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    contactTable = "contacts" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="Name", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    person_name = Entry(labelFrame)
    person_name.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
    lb2 = Label(labelFrame,text="Contact Number", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    contact_number = Entry(labelFrame)
    contact_number.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    
    lb3 = Label(labelFrame,text="Location", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    locat_ion = Entry(labelFrame)
    locat_ion.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=add)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
