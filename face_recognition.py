from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recognisation System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        #**First img
        img_top = Image.open(r"images\face_detection1.jpg")
        img_top = img_top.resize((700,660),Image. Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0, y=45, width=700, height=660)

        #***second img
        img_btm = Image.open(r"images\face_detection2.webp")
        img_btm = img_btm.resize((900,700),Image. Resampling.LANCZOS)
        self.photoimg_btm = ImageTk.PhotoImage(img_btm)

        f_lbl=Label(self.root,image = self.photoimg_btm)
        f_lbl.place(x=700, y=45, width=800, height=680)

         # buttton 
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recg,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=310,y=610,width=200,height=40)



   #  **********************Face Recognition***=========================
    def face_recg(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))    
                

                conn=mysql.connector.connect(host="localhost",username="root",password="Anchal123@",database="face_recognizer")
                my_cursor=conn.cursor()
 

                my_cursor.execute("select Name from student where Student_id=%s", (str(id),))
                n=my_cursor.fetchone()
                n="+".join(n)
                 
                my_cursor.execute("select Roll from student where Student_id=%s", (str(id),))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where Student_id=%s", (str(id),))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img



        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
             break

        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()






































