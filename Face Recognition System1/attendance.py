from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attedance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img=Image.open(r"images/23.jpg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #secound image
        img1=Image.open(r"images/6.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #background image
        img3=Image.open(r"images\15.jpg")
        img3=img3.resize((1530,640))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=640)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("Algerian",25,"bold"),bg="gray",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=520)

        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=750,height=490)

        img_left=Image.open(r"images/30.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=740,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=735,height=325)

        #labels and entrys
        #attedance id
        attedanceId_lable=Label(left_inside_frame,text="AttedanceId:",font=("times new roman",12,"bold"),bg="white")
        attedanceId_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attedanceId_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attedanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #rollno
        rollLable=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLable.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        nameLable=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLable.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #department
        depLable1=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLable1.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)
        
        #time
        timeLable=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLable.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #date
        dateLable=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLable.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        #attendance
        attendanceLable=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLable.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Prasent","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttos frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=735,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        Update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=19,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #Right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=770,y=10,width=720,height=490)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTabl=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTabl.xview)
        scroll_y.config(command=self.AttendanceReportTabl.yview)

        self.AttendanceReportTabl.heading("id",text="Attendance ID")
        self.AttendanceReportTabl.heading("roll",text="Roll")
        self.AttendanceReportTabl.heading("name",text="Name")
        self.AttendanceReportTabl.heading("department",text="Department")
        self.AttendanceReportTabl.heading("time",text="Time")
        self.AttendanceReportTabl.heading("date",text="Date")
        self.AttendanceReportTabl.heading("attendance",text="Attendance")

        self.AttendanceReportTabl["show"]="headings"
        self.AttendanceReportTabl.column("id",width=100)
        self.AttendanceReportTabl.column("roll",width=100)
        self.AttendanceReportTabl.column("name",width=100)
        self.AttendanceReportTabl.column("department",width=100)
        self.AttendanceReportTabl.column("time",width=100)
        self.AttendanceReportTabl.column("date",width=100)
        self.AttendanceReportTabl.column("attendance",width=100)

        self.AttendanceReportTabl.pack(fill=BOTH,expand=1)

        self.AttendanceReportTabl.bind("<ButtonRelease>",self.get_cursor)

        #fetch data 
        def fatchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_childrre())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

        #import csv
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

        #export csv
        def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No Data found to export",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


        def get_cursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

        def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attedance(root)
    root.mainloop()