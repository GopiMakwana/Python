from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER", font=("Algerian",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #top image
        img_top=Image.open(r"images\17.jpg")
        img_top=img_top.resize((1530,750))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=750)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)

        img_top1=Image.open(r"images/32.png")
        img_top1=img_top1.resize((200,250))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=250)

        #developer information
        dev_lable=Label(main_frame,text="Hello! My name is Gopi.",font=("Blackadder ITC",25,"italic"),bg="white")
        dev_lable.place(x=0,y=25)

        dev_lable=Label(main_frame,text="I am Front-end Developer.",font=("Blackadder ITC",20,"italic"),bg="white")
        dev_lable.place(x=0,y=70)

        dev_lable=Label(main_frame,text="I like to craft solid and scalable protend ",font=("times new roman",12,"italic"),bg="white")
        dev_lable.place(x=5,y=140)

        dev_lable=Label(main_frame,text="products with grate user experience.",font=("times new roman",12,"italic"),bg="white")
        dev_lable.place(x=5,y=160)


        #image
        img2=Image.open(r"images/34.jpg")
        img2=img2.resize((500,390))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=260,width=500,height=390)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()