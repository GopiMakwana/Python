from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="May i help you? :)", font=("Algerian",25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #top image
        img_top=Image.open(r"images/36.jpg")
        img_top=img_top.resize((1530,750))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=42,width=1530,height=750)

        dev_lable=Label(f_lbl,text="Email:yellowhack80@gmail.com",font=("times new roman",25,"bold"),bg="white")
        dev_lable.place(x=550,y=355)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()