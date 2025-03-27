from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from time import strftime
from datetime import datetime
import mysql.connector
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Face Recognition System")
        
        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1350, height=45)
        
        # Left Image
        img_left = Image.open(r"D:\smart-class-attendance\smart-class-attendance-\images\images\face1.jpeg")  
        img_left = img_left.resize((600, 650), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        left_lbl = Label(self.root, image=self.photoimg_left)
        left_lbl.place(x=20, y=55, width=600, height=650)
        
        # Right Image
        img_right = Image.open(r"D:\smart-class-attendance\smart-class-attendance-\images\images\8.jpeg") 
        img_right = img_right.resize((600, 650), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        right_lbl = Label(self.root, image=self.photoimg_right)
        right_lbl.place(x=600, y=55, width=650, height=600)
        
        # Button below the right image
        btn = Button(self.root, text="Face Recognition", command=self.recognize_face, font=("times new roman", 20, "bold"), bg="red", fg="white")
        btn.place(x=840, y=600, width=200, height=50)
    
    def mark_attendance(self, student_id, name, department):
        file_path = "attendance.csv"

        # Create file if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("Student_ID,Name,Department,Time,Date,Status\n")

        with open(file_path, "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [entry.split(",")[0] for entry in myDataList]

            if student_id not in name_list:
                now = datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                time_str = now.strftime("%H:%M:%S")
                f.writelines(f"\n{student_id},{name},{department},{time_str},{date_str},Present")
    
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray[y:y + h, x:x + w])
            
            # Confidence Calculation Fix
            confidence = int(100 * (1 - (predict / 300))) if predict > 0 else 100

            # Database Connection
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="face")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student_Name, student_ID, Dep FROM student WHERE Student_id = %s", (id,))
                result = my_cursor.fetchone()

                if result:
                    student_name, student_id, department = result
                else:
                    student_name, student_id, department = "Unknown", "Unknown", "Unknown"

                if confidence > 70:  # Adjusted Confidence Threshold
                    cv2.putText(img, f"Name: {student_name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"ID: {student_id}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dept: {department}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(student_id, student_name, department)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)

                coord = [x, y, w, h]

            except mysql.connector.Error as err:
                print("Database Error:", err)

            finally:
                conn.close()

        return coord

    def recognize(self, img, clf, faceCascade):
        self.draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), clf)
        return img

    def recognize_face(self):
        # Load the Haar cascade classifier
        cascade_path = r"D:\smart-class-attendance\smart-class-attendance-\haarcascade_frontalface_default .xml"
        if not os.path.exists(cascade_path):
            messagebox.showerror("Error", f"Haar Cascade XML file not found at: {cascade_path}")
            return

        faceCascade = cv2.CascadeClassifier(cascade_path)

        # Load the face recognizer model
        model_path = r"D:\smart-class-attendance\smart-class-attendance-\classifier.xml"
        if not os.path.exists(model_path):
            messagebox.showerror("Error", f"Face recognition model file not found at: {model_path}")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(model_path)

        # Open the camera with DirectShow backend
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not cap.isOpened():
            messagebox.showerror("Error", "Could not access webcam. Ensure it is connected and not in use by another app.")
            return

        while True:
            ret, img = cap.read()
            if not ret:
                print("Failed to capture image")
                break

            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
