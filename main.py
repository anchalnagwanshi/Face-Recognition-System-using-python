from tkinter import*
from PIL import Image, ImageTk
import os
from student import Student
from chat import ChatBox
from train import Train
from face_recognition import Face_Recognition

class Face_Recognisation_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recognisation System")
        
         #first image
        img = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\description-3.jpg")
        img = img.resize((455,130),Image. Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image = self.photoimg)
        f_lbl.place(x=0, y=0, width= 455, height=130)

        #2nd img
        img1 = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\face_header_pc.jpg")
        img1 = img1.resize((455,130),Image. Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image = self.photoimg1)
        f_lbl.place(x=455, y=0, width= 455, height=130)

        #3rd img
        img2 = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\face.jpg")
        img2 = img2.resize((450,130),Image. Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image = self.photoimg2)
        f_lbl.place(x=910, y=0, width= 450, height=130)

        #big image
        img3 = Image.open(r"C:\Users\91942\Desktop\face recognisation system\images\background.jpg")
        img3 = img3.resize((1366,688),Image. Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image = self.photoimg3)
        bg_img.place(x=0, y=130, width= 1366, height=688)

        title_lbl=Label(bg_img,text="FACE RECOGNISATION STSYEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        #student button
        img4 = Image.open(r"images\studentDetails.jpg")
        img4 = img4.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command = self.student_details,cursor="hand2")
        b1.place(x=120,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=120,y=280,width=180,height=40)

        #detect face button
        img5 = Image.open(r"images\faceReconition.jpg")
        img5 = img5.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=420,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=420,y=280,width=180,height=40)

        #Attendence button
        img6 = Image.open(r"images\attendence.jpg")
        img6 = img6.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=720,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=720,y=280,width=180,height=40)

        #help button
        img7 = Image.open(r"images\chat.jpg")
        img7 = img7.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,command = self.chat_help,cursor="hand2")
        b1.place(x=1020,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Help",cursor="hand2",command = self.chat_help,font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=1020,y=280,width=180,height=40)

        #train button
        img8 = Image.open(r"images\trainData.jpg")
        img8 = img8.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b1.place(x=120,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=120,y=530,width=180,height=40)

        #photos button
        img9 = Image.open(r"images\photos.jpg")
        img9 = img9.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=420,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=420,y=530,width=180,height=40)

        #Developer button
        img10 = Image.open(r"images\software Developer.jpg")
        img10 = img10.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=720,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=720,y=530,width=180,height=40)

        #exit button
        img11 = Image.open(r"images\exit.jpg")
        img11 = img11.resize((180,180),Image. Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1020,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black")
        b1_1.place(x=1020,y=530,width=180,height=40)

    def open_img(self):
        os.startfile("data")


# ==================================== Fuction Button ==========================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def chat_help(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBox(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognisation_System(root)
    root.mainloop()