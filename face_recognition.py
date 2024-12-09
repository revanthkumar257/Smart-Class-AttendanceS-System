from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from time import strftime
from datetime import datetime
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Face Recognition System")
        
        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1350, height=45)
        
        # Left Image
        img_left = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\BTP NANDINI\smart-class-attendence-system\images\images\face1.jpeg")  # Replace with your actual path
        img_left = img_left.resize((600, 650), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        left_lbl = Label(self.root, image=self.photoimg_left)
        left_lbl.place(x=20, y=55, width=600, height=650)
        
        # Right Image
        img_right = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\BTP NANDINI\smart-class-attendence-system\images\images\8.jpeg")  # Replace with your actual path
        img_right = img_right.resize((600, 650), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        right_lbl = Label(self.root, image=self.photoimg_right)
        right_lbl.place(x=600, y=55, width=650, height=600)
        
        # Button below the right image
        btn = Button(self.root, text="Face Recognition", command=self.recognize_face, font=("times new roman", 20, "bold"), bg="red", fg="white")
        btn.place(x=840, y=600, width=200, height=50)
    
    def mark_attendence(self, i, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [entry.split(",")[0] for entry in myDataList]

            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},present")
    
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray[y:y + h, x:x + w])
            confidence = int((100) * (1 - (predict / 300)))

            conn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                password="Nandini@24", 
                database="face"
            )
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT Student_Name FROM student WHERE Student_id = %s", (id,))
            i = my_cursor.fetchone()
            i = "+".join(i) if i else "Unknown"

            my_cursor.execute("SELECT student_ID FROM student WHERE Student_id = %s", (id,))
            n = my_cursor.fetchone()
            n = "+".join(n) if n else "Unknown"

            my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (id,))
            d = my_cursor.fetchone()
            d = "+".join(d) if d else "Unknown"

            if confidence > 77:
                cv2.putText(img, f"Name: {i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Dep: {d}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"student_ID: {n}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendence(i, n, d)
            else:
                cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)

            coord = [x, y, w, h]

        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
        return img

    def recognize_face(self):
        faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")  # Ensure path is correct
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # Replace with the correct path to your classifier file

        cap = cv2.VideoCapture(0)  # Start the webcam

        while True:
            ret, img = cap.read()
            if not ret:
                break

            img = self.recognize(img, clf, faceCascade)  # Recognize faces
            cv2.imshow("Face Recognition", img)  # Display the video feed with detected faces

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()