from tkinter import *
from os import path

def login():
    userID = str(userIDEntry.get())
    pw = str(pwEntry.get())

    dir = "database/"+userID+".txt"
    res = path.exists(dir)
    if(res==True):
        file = open(dir)
        content = file.readlines()
        password = content[4]

        if(password==pw):
            msg = "Login Granted       "
            msgLabel = Label(window2,text=msg,fg="Green",font=("Cambria",12))
            msgLabel.place(x=110,y=90)

        else: 
            msg = "Invalid Password      "
            msgLabel = Label(window2,text=msg,fg="Red",font=("Cambria",12))
            msgLabel.place(x=110,y=90)

    else :
        msg = "User doesn't exist     "
        msgLabel = Label(window2,text=msg,fg="Red",font=("Cambria",12))
        msgLabel.place(x=110,y=90)

def register():
    name = str(nameEntry.get())
    mobile = str(mobileEntry.get())
    email = str(emailEntry.get())
    userID = str(userEntry.get())
    pwd = str(pwdEntry.get())

    temp = "database/"+userID + ".txt"
    file = open(temp,"a+")
    file.write(name+"\n"+mobile+"\n"+email+"\n"+userID+"\n"+pwd)
    file.close()
    window1.destroy()

    func()
    

def regWindow():
    window.destroy()
    
    global window1
    window1 = Tk()
    window1.geometry("350x350")
    window1.title("Student Dashboard")
    window1.config(bg="purple")

    heading = Label(window1,text="Register User",font=("Times New Roman",30))
    heading.place(x=70,y=5)

    canvas = Canvas(window1,height=250,width=300)
    canvas.place(x=25,y=75)

    #   (25,75) (325,75)    (25,325) (325,325)
    #canvas.create_rectangle(35,15,270,235,fill="blue")
    canvas.create_rectangle(0,0,325,325,fill="light gray")

    nameLabel = Label(canvas,text="Name : ",font=("Times New Roman",12))
    nameLabel.place(x=10,y=10)

    global nameEntry
    nameEntry = Entry(canvas,width="15",font=("Times New Roman",12))
    nameEntry.place(x=135,y=10)

    mobileLabel = Label(canvas,text="Mobile Number : ",font=("Times New Roman",12))
    mobileLabel.place(x=10,y=40)

    global mobileEntry
    mobileEntry = Entry(canvas,width="15",font=("Times New Roman",12))
    mobileEntry.place(x=135,y=40)

    emailLabel = Label(canvas,text="Email ID : ",font=("Times New Roman",12))
    emailLabel.place(x=10,y=70)

    global emailEntry
    emailEntry = Entry(canvas,width="15",font=("Times New Roman",12))
    emailEntry.place(x=135,y=70)

    canvas.create_line(10,110,290,110)

    userLabel = Label(canvas,text="USER ID : ",font=("Times New Roman",13))
    userLabel.place(x=10,y=130)

    global userEntry
    userEntry = Entry(canvas,width="15",font=("Times New Roman",12))
    userEntry.place(x=135,y=130)

    pwdLabel = Label(canvas,text="PASSWORD : ",font=("Times New Roman",13))
    pwdLabel.place(x=10,y=165)

    global pwdEntry
    pwdEntry = Entry(canvas,width="15",font=("Times New Roman",12))
    pwdEntry.place(x=135,y=165)

    submitBtn = Button(canvas,text="Sign Up",font=("Times New Roman",12),command=register)
    submitBtn.place(x=110,y=205)

    window1.mainloop()

def loginWindow():
    window.destroy()
    
    global window2
    window2 = Tk()
    window2.geometry("350x170")
    window2.title("Student Login Dashboard")
    window2.config(bg="Sky Blue")

    userLabel = Label(window2,text="User ID :",font=("Times New Roman",13))
    userLabel.place(x=50,y=20)

    global userIDEntry
    userIDEntry = Entry(window2,width="15",font=("Times New Roman",13))
    userIDEntry.place(x=135,y=20)

    pwdLabel = Label(window2,text="Password :",font=("Times New Roman",13))
    pwdLabel.place(x=50,y=60)

    global pwEntry
    pwEntry = Entry(window2,width="15",font=("Times New Roman",13))
    pwEntry.place(x=135,y=60)

    submitBtn = Button(window2,text="Login",font=("Times New Roman",13),bg="Black",fg="White",command=login)
    submitBtn.place(x=150,y=120)

    window2.mainloop()
    
def func():        
    global window
    window = Tk()
    window.title("Student Dashboard")

    window.config(bg="Violet")

    btn1 = Button(window,text="Sign Up",font=("Times New Roman",15),bg="Black",fg="White",command=regWindow)
    btn1.place(x=55,y=25)

    btn2 = Button(window,text="Login",font=("Times New Roman",15),bg="Black",fg="White",command=loginWindow)
    btn2.place(x=65,y=75)


func()
