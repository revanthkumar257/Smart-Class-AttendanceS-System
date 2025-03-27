from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from time import strftime
from datetime import datetime

import os

class FACE_RECOGNITION:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load and resize images
        self.photoimg1 = self.load_image(r"C:\Users\srave\Desktop\images - Copy\1.jpg", (500, 130))
        self.photoimg2 = self.load_image(r"C:\Users\srave\Desktop\images - Copy\2.jpeg", (500, 130))
        self.photoimg3 = self.load_image(r"C:\Users\srave\Desktop\images - Copy\3.jpeg", (500, 130))
        self.photoimg_bg = self.load_image(r"C:\Users\srave\Desktop\images - Copy\4.jpg", (1530, 710))

        # Display header images
        if self.photoimg1: Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        if self.photoimg2: Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
        if self.photoimg3: Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=530, height=130)

        # Display background image
        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title label
        title_lbl = Label(bg_img, text="SMART CLASS ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ===================== Time =======================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # Create buttons
        self.create_buttons(bg_img)

    def load_image(self, path, size):
        """Load and resize image."""
        if not os.path.exists(path):
            messagebox.showerror("Error", f"File not found: {path}")
            return None
        img = Image.open(path).resize(size, Image.Resampling.LANCZOS)  # Updated for new Pillow versions
        return ImageTk.PhotoImage(img)

    def create_buttons(self, bg_img):
        """Create all the buttons on the main screen."""
        button_config = [
            ("Student Details", r"C:\Users\srave\Desktop\images - Copy\student.jpg", self.student_details),
            ("Face Detector", r"C:\Users\srave\Desktop\images - Copy\face2.jpeg", self.face_data),
            ("Attendance", r"C:\Users\srave\Desktop\images - Copy\6.jpeg", self.attendance),
            ("Help Desk", r"C:\Users\srave\Desktop\images - Copy\7.png", self.help),
            ("Train Data", r"C:\Users\srave\Desktop\images - Copy\8.jpeg", self.train_data),
            ("Photos", r"C:\Users\srave\Desktop\images - Copy\9.jpeg",self.open_img),
            ("Developer", r"C:\Users\srave\Desktop\images - Copy\10.jpeg", self.developer),
            ("Exit", r"C:\Users\srave\Desktop\images - Copy\11.jpeg", self.exit_system)
        ]

        # Button layout
        x, y = 100, 100
        for i, (text, img_path, command) in enumerate(button_config):
            if i == 4:  # Move to next row
                x, y = 100, 300
            self.create_button(bg_img, img_path, text, x, y, command)
            x += 260

    def create_button(self, bg_img, img_path, text, x, y, command):
        """Create a button with image and text."""
        img = self.load_image(img_path, (150, 150))
        if img:
            btn = Button(bg_img, image=img, cursor="hand2", command=command)
            btn.image = img  # Keep a reference to the image
            btn.place(x=x, y=y, width=160, height=160)
            Button(bg_img, text=text, command=command, font=("times new roman", 10, "bold"), bg="white", fg="red").place(x=x, y=y + 160, width=160, height=30)

    # Button actions
    def open_img(self):
        os.startfile("data")


    def student_details(self):
        if hasattr(self, 'student_window') and self.student_window.winfo_exists():
            self.student_window.lift()  # Bring the existing window to the front
        else:
            self.student_window = Toplevel(self.root)
            self.app = Student(self.student_window)

    def face_detector(self):
        messagebox.showinfo("Info", "Face Detector functionality not implemented")

    def attendance(self):
        if hasattr(self, 'attendance_window') and self.attendance_window.winfo_exists():
            self.attendance_window.lift()  # Bring the existing window to the front
        else:
            self.attendance_window = Toplevel(self.root)
            self.app = Attendance(self.attendance_window)
        messagebox.showinfo("Info", "Attendance functionality not implemented")

    def help(self):
        if hasattr(self, 'help_window') and self.help_window.winfo_exists():
            self.help_window.lift()  # Bring the existing window to the front
        else:
            self.help_window = Toplevel(self.root)
            self.app = Help(self.help_window)

    def train_data(self):
        self.help_window = Toplevel(self.root)
        self.app = Train(self.help_window)
    
    def face_data(self):
        self.help_window = Toplevel(self.root)
        self.app = Face_Recognition(self.help_window)
        

    def photos(self):
        messagebox.showinfo("Info", "Photos functionality not implemented")

    def developer(self):
        if hasattr(self, 'developer_window') and self.developer_window.winfo_exists():
            self.developer_window.lift()  # Bring the existing window to the front
        else:
            self.developer_window = Toplevel(self.root)
            self.app = Developer(self.developer_window)

    def exit_system(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = FACE_RECOGNITION(root)
    root.mainloop()
