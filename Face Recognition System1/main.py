from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student 
import os
from train import Train
from face_recognition import Face_Recognition 
from attendance import Attedance
from developer import Developer
from help import Help
import tkinter

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
    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()