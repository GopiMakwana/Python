from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

from student import Student
import os
from train import Train
from face_recognition import Face_Recognition 
from attendance import Attedance
from developer import Developer
from help import Help
import tkinter

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img=Image.open(r"images/37.png")
        img=img.resize((1530,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=800)

        frame=LabelFrame(self.root,bd=2,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"images/16.png")
        img1=img1.resize((100,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1,borderwidth=0,bg="black")
        lblimg1.place(x=730,y=125,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Blackadder ITC",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=60)

        #labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtemail=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="white")
        self.txtemail.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="white")
        self.txtpass.place(x=40,y=250,width=270)

        #icon images
        img2=Image.open(r"images/16.png")
        img2=img2.resize((23,23))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg1=Label(self.root,image=self.photoimg2,borderwidth=0,bg="black")
        lblimg1.place(x=655,y=323,width=25,height=25)

        img3=Image.open(r"images/40.png")
        img3=img3.resize((23,23))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,borderwidth=0,bg="black")
        lblimg1.place(x=655,y=395,width=25,height=25)

        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=30)

        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forget password button
        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=10,y=370,width=160)

    #define for register window
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

        self.txtemail=StringVar()
        self.txtpass=StringVar()

    def login(self):
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required.")
        elif self.txtemail.get()=="gopi" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Welcome :)   I am face recognition.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="gopi0987",database="face_recognition1")
            my_cursor=conn.cursor()
            
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                            self.txtemail.get(),
                                                                            self.txtpass.get()
                                                                            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password.")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin.")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
#--------------------------------------------------------------------------------------------------------
    #reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question.",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer.",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password.",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="gopi0987",database="face_recognition1")
            my_cursor=conn.cursor()
            query="select * from reregister where email=%s and securityQ=%s and securityA=%s"
            value=(self.txtuser.get(),self.combo_security_Q.get,self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer.",parent=self.root2)
            else:
                query=("update register set password=%s whrere email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()




#--------------------------------------------------------------------------------------------------------
    #forget password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="gopi0987",database="face_recognition1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if  row==None:
                messagebox.showerror["My Error","Please enter the valid user name."]
            else: 
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Passwod")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(self.root2,text="Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your birth place?","Your fevourite food?","Your fevourite place?","Your fevourite cousin?")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)        

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=140,y=290)



#-------------------------------------------------------------------------------------------------------
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
        b1=Button(frame,image=self.photoimg3,command=self.return_login,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
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

    def return_login(self):
        self.root.destroy()

#-------------------------------------------------------------------------------------------------------

class Face_Recognition_System:  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"images\1.jpg")
        img=img.resize((505,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=505,height=130)

        #secound image
        img1=Image.open(r"images\2.jpg")
        img1=img1.resize((505,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=505,y=0,width=505,height=130)

        #third image
        img2=Image.open(r"images\21.jpg")
        img2=img2.resize((505,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1010,y=0,width=505,height=130)

        #background image
        img3=Image.open(r"images\15.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Algerian",25,"bold"),bg="blue",fg="ivory")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"images\24.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detact face
        img5=Image.open(r"images\3.png")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2", font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance face button
        img6=Image.open(r"images\23.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help
        img7=Image.open(r"images\25.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train
        img8=Image.open(r"images\5.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data, font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=200,y=580,width=220,height=40)

        #photos
        img9=Image.open(r"images\13.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer
        img10=Image.open(r"images\26.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        #exit
        img11=Image.open(r"images\18.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"italic"),bg="coral",fg="navy")
        b1_1.place(x=1100,y=580,width=220,height=40)

    #click on photo9 butto for open photos folder (data)
    def open_img(self):
        os.startfile("data")

    #exit
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project?", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


    #----------functions buttons---------- 
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    #functions buttons for train
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    #functions buttons for face_recohnition
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    #functions buttons for attendance
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attedance(self.new_window)

    #functions buttons for developer
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    #functions buttons for help
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    

#-------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()