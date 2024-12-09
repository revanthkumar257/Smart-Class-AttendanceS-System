from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #====================variables============================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        
        # Load and resize images
        img = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\2.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\3.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=400, height=130)

        img3 = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\4.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=50, width=1450, height=650)

        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=600, height=630)

        # Current course frame
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=3, y=5, width=590, height=120)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=5, pady=5)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("select dept", "CSE", "IT", "MNC", "CSD", "Petroleum", "CHE", "EE", "EV")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5)

        # Course
        Course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        Course_label.grid(row=0, column=2, padx=5, pady=5)
        Course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        Course_combo["values"] = ("select Course", "maths", "web", "AI", "robotics")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=3, padx=5, pady=5)

        # Year and Semester
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=5, pady=5)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("select year", "1", "2", "3", "4")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5)

        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=5, pady=5)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("select semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=5)

        # Class student info
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=3, y=130, width=590, height=170)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5)
        studentID_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_id, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=5, pady=5)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=5)
        studentName_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5)

        # Phone No
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=1, column=0, padx=5, pady=5)
        phone_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_phone, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=1, column=1, padx=5, pady=5)

        # Email
        email_label = Label(class_student_frame, text="Email ID:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=1, column=2, padx=5, pady=5)
        email_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        email_entry.grid(row=1, column=3, padx=5, pady=5)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=5)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("select gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5)
         
        # Radio Buttons
        self.var_radio = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, text="Take photo sample", variable=self.var_radio, value="Yes")
        radiobtn1.grid(row=2, column=2, padx=5, pady=5)
        radiobtn2 = ttk.Radiobutton(class_student_frame, text="No photo sample", variable=self.var_radio, value="No")
        radiobtn2.grid(row=2, column=3, padx=5, pady=5)

        # Button frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=300, width=580, height=40)

        save_btn = Button(btn_frame, text="Save", width=12, command=self.add_data)
        save_btn.grid(row=0, column=0, padx=1)

        update_btn = Button(btn_frame, text="Update", width=12, command=self.update_student)
        update_btn.grid(row=0, column=1, padx=1)

        delete_btn = Button(btn_frame, text="Delete", width=12, command=self.delete_student)
        delete_btn.grid(row=0, column=2, padx=1)

        reset_btn = Button(btn_frame, text="Reset", width=12, command=self.reset)
        reset_btn.grid(row=0, column=3, padx=1)
                # Buttons for taking and updating photo samples
        photo_btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        photo_btn_frame.place(x=0, y=360, width=590, height=40)

        take_photo_btn = Button(photo_btn_frame,command=self.generate_dataset, text="Take Photo Sample", font=("times new roman", 13, "bold"), width=24, bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)
        update_photo_btn=Button(photo_btn_frame,text="update photo Sample",font=("times new roman",13,"bold"),width=24,bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        # Right frame for displaying student records
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=620, y=10, width=820, height=630)

        # Search system
        search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=5, y=5, width=800, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Student ID", "Phone No", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5)

        search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"), width=12, bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5, pady=5)

        show_all_btn = Button(search_frame, text="Show All", font=("times new roman", 12, "bold"), width=12, bg="blue", fg="white")
        show_all_btn.grid(row=0, column=4, padx=5, pady=5)

        # Table frame for displaying student records with scrollbars
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=80, width=800, height=540)


        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "semester", "id", "name", "phone", "email", "gender", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("email", text="Email ID")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("photo", text="Photo Sample")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):  # Fixed indentation
        if self.var_dep.get() == "select dept" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Placeholder for adding data functionality
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Nandini@24",
                    database="face"
                )
                if conn.is_connected():
                    my_cursor = conn.cursor()

                    # Execute insert statement
                    my_cursor.execute("""
                        INSERT INTO student (dep, course, year, semester, student_id, student_Name, phone_No, Email_ID, gender,Takephotosample) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_radio.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Student details have been successfully added", parent=self.root)
                else:
                    messagebox.showerror("Error", "Failed to connect to the database", parent=self.root)

            except Exception as es:  # Changed Error to Exception
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

            finally:
                if conn.is_connected():
                    conn.close()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Nandini@24", database="face")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_semester.set(row[3])
        self.var_id.set(row[4])
        self.var_name.set(row[5])
        self.var_phone.set(row[6])
        self.var_email.set(row[7])
        self.var_gender.set(row[8])

    def update_student(self):
        if self.var_dep.get() == "select dept" or self.var_course.get() == "select Course" or self.var_year.get() == "select year" or self.var_semester.get() == "select semester" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_phone.get() == "" or self.var_email.get() == "" or self.var_gender.get() == "select gender":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Nandini@24", database="face")
                cursor = conn.cursor()
                cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, student_Name=%s, phone_No=%s, Email_ID=%s, Gender=%s WHERE student_ID=%s", 
                               (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_name.get(), self.var_phone.get(), self.var_email.get(), self.var_gender.get(), self.var_id.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def delete_student(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Nandini@24", database="face")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM student WHERE student_id=%s", (self.var_id.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details deleted successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def reset(self):
        self.var_dep.set("select dept")
        self.var_course.set("select Course")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_gender.set("select gender")
        self.var_radio.set("")
#====================generate photo sample======================================

    def generate_dataset(self):
    # Check if any required fields are empty
        if (self.var_dep.get() == "select dept" or 
            self.var_course.get() == "select Course" or 
            self.var_year.get() == "select year" or 
            self.var_semester.get() == "select semester" or 
            self.var_id.get() == "" or 
            self.var_name.get() == "" or 
            self.var_phone.get() == "" or 
            self.var_email.get() == "" or 
            self.var_gender.get() == "select gender"):
            
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="Nandini@24", 
                    database="face"
                )
                my_cursor = conn.cursor()

                # Update student data
                my_cursor.execute(
                    "UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, student_Name=%s, "
                    "phone_No=%s, Email_ID=%s, Gender=%s WHERE student_ID=%s",
                    (
                        self.var_dep.get(), 
                        self.var_course.get(), 
                        self.var_year.get(), 
                        self.var_semester.get(),
                        self.var_name.get(), 
                        self.var_phone.get(), 
                        self.var_email.get(), 
                        self.var_gender.get(), 
                        self.var_id.get()
                    )
                )
                conn.commit()
                conn.close()
                
                # Initialize face detection
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    if len(faces) == 0:  # No face detected
                        return None
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]

                # Ensure the data directory exists
                if not os.path.exists("data"):
                    os.makedirs("data")

                # Capture images
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        print("Failed to capture frame")
                        break  # If the frame is not captured correctly, exit the loop
                    
                    # Get the cropped face
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # Save the image with a unique name
                        file_name_path = f"data/user.{self.var_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)

                        # Display the frame with image ID
                        cv2.putText(face, str(img_id), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Face Capture", face)

                    # Break after capturing 100 images or on 'Enter' key
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                # Release the camera and destroy windows
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result", f"Dataset generated for Student ID: {self.var_id.get()}", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
