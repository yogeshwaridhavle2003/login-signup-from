from customtkinter import*
from tkinter import messagebox
import pymysql

def login_user():
    if login_emailEntry.get() == '' or login_password1Entry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Dhavle@2427')
            cur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity issue, Please try again')
            return

        cur.execute('USE customer_info')
        
        cur.execute('SELECT * FROM data WHERE email=%s AND password=%s', 
                    (login_emailEntry.get(), login_password1Entry.get()))
        
        record = cur.fetchone()
        if record is None:
            messagebox.showerror('Error', 'Invalid details')
        else:
            messagebox.showinfo('Success', 'Login Successful')
        
        con.close()



def signup_user():
    if nameEntry.get()== '' or emailEntry.get()=='' or password1Entry.get()=='' or password2Entry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif password1Entry.get()!= password2Entry.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Dhavle@2427')
            cur=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity issue,Please try again')
            return
        try:
            cur.execute(query='CREATE DATABASE customer_info')
            cur.execute('USE customer_info')
            cur.execute('CREATE TABLE data(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,email VARCHAR (50),name VARCHAR (100),password VARCHAR(50))')
        except:  
            cur.execute('USE customer_info')

        cur.execute('SELECT * from data where email=%s',(emailEntry.get()))
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror('Error','Email already exists')
        else:


           cur.execute('INSERT INTO data(email,name,password) values(%s,%s,%s)',(emailEntry.get(),nameEntry.get(),password1Entry.get()))
           con.commit()

           con.close()
           messagebox.showinfo('Success','Registration is Successful')
           login_page()


def signup_page():
    loginFrame.grid_forget()
    signup_window.geometry('400x500+300+100')
    signup_window.title('Signup Window')
    signupFrame.grid(row=0,column=0,pady=30)

def login_page():
    global loginFrame,login_emailEntry,login_password1Entry
    signupFrame.grid_forget()
    signup_window.title('Login Window')
    signup_window.geometry('400x370+300+100')

    loginFrame=CTkFrame(signup_window,fg_color='white')
    loginFrame.grid(row=0,column=0,pady=30)
     
    headingLabel=CTkLabel(loginFrame,text='Welcome Back',font=('bookman old style',40,'bold'),text_color='gray20')
    headingLabel.grid(row=0,column=0)

    subheadingLabel=CTkLabel(loginFrame,text='Log in to access your account',font=('bookman old style',20,'bold'),text_color='gray20')
    subheadingLabel.grid(row=1,column=0,pady=(0,20))

    login_emailEntry=CTkEntry(loginFrame,placeholder_text='Enter Email',font=('bookman old style',20),height=40,width=380)
    login_emailEntry.grid(row=2,column=0,padx=10,pady=(0,20))

    login_password1Entry=CTkEntry(loginFrame,placeholder_text='Enter Password',font=('bookman old style',20),height=40,width=380,show='*')
    login_password1Entry.grid(row=3,column=0,padx=10,pady=(0,20))

    loginButton=CTkButton(loginFrame,text='Login',width=380,height=40,font=('bookman old style',20,'bold'),text_color='white',cursor='hand2',command=login_user)
    loginButton.grid(row=4,column=0,pady=(0,20))

    frame=CTkFrame(loginFrame,fg_color='white')
    frame.grid(row=7,column=0)

    memberLabel=CTkLabel(frame,text='Not a member',font=('bookman old style',20,'bold'),text_color='gray20')
    memberLabel.grid(row=0,column=0)

    signuphereButton=CTkButton(frame,text='signup Here',font=('bookman old style',20,'underline'),text_color='white',hover_color='white',cursor='hand2',command=signup_page)
    signuphereButton.grid(row=0,column=1)



signup_window=CTk()
signup_window.title('Signup Window')
signup_window.geometry('400x500+300+100')
signup_window.resizable(0,0)
signup_window.configure(fg_color='white')

signupFrame=CTkFrame(signup_window,fg_color='white')
signupFrame.grid(row=0,column=0,pady=30 )

headingLabel=CTkLabel(signupFrame,text='Join us today',font=('bookman old style',40,'bold'),text_color='gray20')
headingLabel.grid(row=0,column=0)

subheadingLabel=CTkLabel(signupFrame,text='Sign up now to become a member',font=('bookman old style',20,'bold'),text_color='gray20')
subheadingLabel.grid(row=1,column=0,pady=(0,20))

nameEntry=CTkEntry(signupFrame,placeholder_text='Enter Name',font=('bookman old style',20),height=40,width=380)
nameEntry.grid(row=2,column=0,padx=10,pady=(0,20))

emailEntry=CTkEntry(signupFrame,placeholder_text='Enter Email',font=('bookman old style',20),height=40,width=380)
emailEntry.grid(row=3,column=0,padx=10,pady=(0,20))

password1Entry=CTkEntry(signupFrame,placeholder_text='Choose a Password',font=('bookman old style',20),height=40,width=380,show='*')
password1Entry.grid(row=4,column=0,padx=10,pady=(0,20))

password2Entry=CTkEntry(signupFrame,placeholder_text='Re-Enter Password',font=('bookman old style',20),height=40,width=380,show='*')
password2Entry.grid(row=5,column=0,padx=10,pady=(0,20))

signupButton=CTkButton(signupFrame,text='Signup',width=380,height=40,font=('bookman old style',20,'bold'),text_color='white',cursor='hand2',command=signup_user)
signupButton.grid(row=6,column=0,pady=(0,20))

frame=CTkFrame(signupFrame,fg_color='white')
frame.grid(row=7,column=0)

memberLabel=CTkLabel(frame,text='Already a member',font=('bookman old style',20,'bold'),text_color='gray20')
memberLabel.grid(row=0,column=0)

loginhereButton=CTkButton(frame,text='Login Here',font=('bookman old style',20,'underline'),text_color='white',hover_color='white',cursor='hand2',command=login_page)
loginhereButton.grid(row=0,column=1)



signup_window.mainloop()