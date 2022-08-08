from tkinter import *

def save_mail():
    mail=emailA.get()
    userLabel.config(text="", bg="#BF8A6B")
    try:
        mailA=mail.split('@')
        user=mailA[0].replace(" ","")
        domain=mailA[1].replace(" ","")

        userLabel.config(text="The username is "+ user + " & the domain is "+domain, bg="#BF8A6B")   
        emailA.delete(0, END)

    except:
        userLabel.config(text="Insert a valid adress", bg="#BF8A6B")     
        emailA.delete(0, END)
        return


root=Tk()
root.title("Email Slicer")
root.geometry('400x200')
root.config(bg="#F2F2F0")

your=Label(root,text="Insert your email adress:")
your.grid(row=1,column=0, pady=10)

emailA=Entry(root, width=60)
emailA.grid(row=2,column=0,padx=20)

enter=Button(root, text="Enter", padx=10, pady=2, bg="#BFB8AA", command=save_mail)
enter.grid(row=3,column=0,pady=20)

userLabel=Label(root, text="")
userLabel.grid(row=4, column=0, pady=10)

root.mainloop()