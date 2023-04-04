from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recognisation System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        img_top = Image.open(r"images\face_header_pc.jpg")
        img_top = img_top.resize((1530,280),Image. Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0, y=55, width= 1480,height=720)

        #frame
        main_frame=Frame(f_lbl, bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=450,height=600)

        img_top1 = Image.open(r"images\face_header_pc.jpg")
        img_top1 = img_top1.resize((200,200),Image. Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image = self.photoimg_top1)
        f_lbl.place(x=250, y=0, width= 200,height=200)

        #developer info
        dep_label=Label(main_frame,text="hello my name is, anchal",font=("times new roman",20,"bold"),bg="white")
        dep_label.place(x=0,y=5)

        dep_label=Label(main_frame,text="I am full stack developer",font=("times new roman",20,"bold"),bg="white")
        dep_label.place(x=0,y=40)






if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()