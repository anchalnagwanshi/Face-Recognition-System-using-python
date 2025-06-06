from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recognisation System")


        #===========================variables=============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



#first image
        img = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\description-3.jpg")
        img = img.resize((455,100),Image. Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image = self.photoimg)
        f_lbl.place(x=0, y=0, width= 455, height=100)

        #2nd img
        img_left = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\face_header_pc.jpg")
        img_left = img_left.resize((455,100),Image. Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image = self.photoimg_left)
        f_lbl.place(x=455, y=0, width= 455, height=100)

        #3rd img
        img2 = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\face.jpg")
        img2 = img2.resize((450,100),Image. Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image = self.photoimg2)
        f_lbl.place(x=910, y=0, width= 450, height=100)
         
         #big image
        img3 = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\background.jpg")
        img3 = img3.resize((1366,688),Image. Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image = self.photoimg3)
        bg_img.place(x=0, y=100, width= 1366, height=688)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10, y=60,width=1330,height=550)

        #left label frame
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=520)
       
        img_left = Image.open(r"images\student1.jpg")
        img_left = img_left.resize((720,100),Image. Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5, y=0, width= 645,height=80)


        # current course information
        current_course_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=80,width=640,height=115)

        #departmenet
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select course","BE","BTECH","MTECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select year","2019-2023","2020-2024","2021-2025","2022-2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # class student information information
        class_student_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=195,width=640,height=300)

        #student_id
        StudentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student_name
        StudentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll No
        roll_no_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # date of birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        add_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample", value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample", value="No")
        radiobtn2.grid(row=5,column=1)

        #button frames
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0, y=214,width=640,height=40)

        save_btn=Button(button_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,text="Update",width=17,command=self.update_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(button_frame,text="Delete",width=17,command=self.delete_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(button_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=3)

        button_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=0, y=250,width=640,height=35)

        take_photo_btn=Button(button_frame1,command=self.genrate_dataset,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="black",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(button_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="black",fg="white")
        update_photo_btn.grid(row=1,column=1)

        #rigth label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font="ariel 12 bold")
        Right_frame.place(x=670,y=10,width=650,height=520)

        img_right= Image.open(r"images\student2.jpg")
        img_right = img_right.resize((720,100),Image. Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5, y=0, width= 680,height=80)

        #===========search system==========
        search_frame=LabelFrame(Right_frame,bg="white",bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=85,width=640,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="black",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="black",fg="white")
        showAll_btn.grid(row=0,column=4)

        #==================table frame==================
        tabel_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        tabel_frame.place(x=5,y=175,width=640,height=300)

        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(tabel_frame,columns=("dep","course","year","sem","Id","Name","div","RollNo","gender","dob","email","phone","address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("Id",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("RollNo",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DateOfBirth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="PhoneNo")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"
       
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=130)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()






#============fucntion declaration===========================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Anchal123@',database="face_recognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()

                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    #===========================fetch data =========================================
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Anchal123@',database="face_recognizer")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==========================get cursor=======================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#================update function==============================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if upadate>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Anchal123@',database="face_recognizer")
                    my_cursor= conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
 
                                                                                                                                                                                     self.var_dep.get(), 
                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                                     self.var_std_name.get(),
                                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                     self.var_std_id.get()
                                                                                                                                                                                ))
                else:
                    if not upadate:
                        return 
                messagebox.showinfo("Success", "Student details successfullly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


 #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you wsant to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Anchal123@',database="face_recognizer")
                    my_cursor= conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#===========genrating data set or take photo sample=======================
    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Anchal123@',database="face_recognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s, course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
 
                                                                                                                                                                                     self.var_dep.get(), 
                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                                     self.var_std_name.get(),
                                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                     self.var_std_id.get()==id+1
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
    #============load predefined data on face frontals from opencv====================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
        #scaling factor=1.3
        #minimum neighbour=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+","+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genrating data sets compled!!!!!!")    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()