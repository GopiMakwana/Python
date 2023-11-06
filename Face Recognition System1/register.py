from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #background image
        img=Image.open(r"images/5.jpg")
        img=img.resize((1530,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=800)

        #left image
        img1=Image.open(r"images/19.jpg")
        img1=img1.resize((470,550))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #register lable
        register_lbl=Label(frame,text="REGISTER HERE",font=("Algerian",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        #lables and entrys
        #1row
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #2row
        contact=Label(frame,text="Cotact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #3row
        security_Q=Label(frame,text="Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place?","Your fevourite food?","Your fevourite place?","Your fevourite cousin?")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)        

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #4row
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions.",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        img2=Image.open("images/41.jpg")
        img2=img2.resize((200,40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=10,y=420,width=300)

        img3=Image.open("images/42.jpg")
        img3=img3.resize((200,40))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimg3,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=330,y=420,width=300)


    #function declaration
    def register_data(self):  
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required.")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same.")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="gopi0987",database="face_recognition1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                    ))
                
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfully.")



if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()