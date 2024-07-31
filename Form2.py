from tkinter import * 
from tkinter import messagebox
import mysql.connector

def Insert():
    name=e1.get()
    email=e2.get()
    password=e3.get()
    number=e4.get()
    if(name=="" or email=="" or password=="" or number==""):
        messagebox.showinfo("insert status","please fill complete data")
    else:
        con=mysql.connector.connect(host="localhost",user="root",password="sunil123",database="gui2")
        cur=con.cursor()
        query="insert into guidata(name,email,password,number) values(%s,%s,%s,%s)"
        values=[(name,email,password,number)]
        cur.executemany(query,values)
        con.commit()
        messagebox.showinfo("insert status","your data has been inserted successfully")
def Update():
    name=e1.get()
    email=e2.get()
    password=e3.get()
    number=e4.get()
    if(name=="" or email=="" or password=="" or number==""):
        messagebox.showinfo("update status","please fill complete data")
    else:
        con=mysql.connector.connect(host="localhost",user="root",password="sunil123",database="gui2")
        cur=con.cursor()
        query=f"update guidata set name='{name}',email='{email}',password='{password}',number='{number}' where name='{name}'"
        cur.execute(query)
        con.commit()
        messagebox.showinfo("update status","your data has been updated successfully")
def Delete():
    name=e1.get()
    email=e2.get()
    password=e3.get()
    number=e4.get()
    if(email==""):
        messagebox.showinfo("delete status","please fill email data")
    else:
        con=mysql.connector.connect(host="localhost",user="root",password="sunil123",database="gui2")
        cur=con.cursor()
      
        query=f"delete from guidata where email='{email}'"
        cur.execute(query)
        con.commit()
        messagebox.showinfo("delete status","your data has been deleted successfully")

root=Tk()

root.geometry("800x800")

root.title("form ")

l1=Label(root,text="Login Form",font='verdana 35 bold',bg="black",fg="white")
l1.place(x=0,y=0,width=800)

l2=Label(root,text="username",font=("verdana 25 bold"),fg="black")
l2.place(x=100,y=100,width=250)

e1=Entry(root,text="",font=("verdana 25 bold"),fg="black")
e1.place(x=380,y=100,width=400)


l2=Label(root,text="useremail",font=("verdana 25 bold"),fg="black")
l2.place(x=100,y=200,width=250)

e2=Entry(root,text="",font=("verdana 25 bold"),fg="black")
e2.place(x=380,y=200,width=400)


l2=Label(root,text="userpassword",font=("verdana 25 bold"),fg="black")
l2.place(x=100,y=300,width=270)

e3=Entry(root,text="",font=("verdana 25 bold"),fg="black")
e3.place(x=380,y=300,width=400)

l2=Label(root,text="userNumber",font=("verdana 25 bold"),fg="black")
l2.place(x=100,y=400,width=250)

e4=Entry(root,text="",font=("verdana 25 bold"),fg="black")
e4.place(x=380,y=400,width=400)

# l2=Label(root,text="Subjects",font=("verdana 25 bold"),fg="black")
# l2.place(x=100,y=500,width=250)

# b1=Radiobutton(root,padx=100,pady=100,width=100,height=20)
# b1.place(x=380,y=500,width=100)


b1=Button(root,text="login",font=("verdana 25 bold "),bg="red",fg="white",command=Insert)
b1.place(x=100,y=500,width=150)
b2=Button(root,text="update",font=("verdana 25 bold "),bg="green",fg="black",command=Update)
b2.place(x=280,y=500,width=150)
b3=Button(root,text="delete",font=("verdana 25 bold "),bg="blue",fg="white",command=Delete)
b3.place(x=450,y=500,width=150)

root.mainloop()