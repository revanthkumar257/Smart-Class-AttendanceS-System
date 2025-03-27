from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from main import FACE_RECOGNITION

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.state('zoomed')

        # Load the background image safely
        try:
            self.bg_image = Image.open(r"D:\smart-class-attendance\smart-class-attendance-\images\images\login.jpg")
            self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        except Exception as e:
            messagebox.showerror("Error", f"Background image not found: {str(e)}")
            return

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for Login Form
        frame = Frame(self.root, bg="white", bd=5, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=400, height=500)

        title = Label(frame, text="Login Here", font=("Arial", 25, "bold"), bg="white", fg="darkblue")
        title.pack(pady=20)

        Label(frame, text="Username", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.username_entry = Entry(frame, font=("Arial", 15))
        self.username_entry.pack(pady=5)

        Label(frame, text="Password", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        self.password_entry = Entry(frame, font=("Arial", 15), show='*')
        self.password_entry.pack(pady=5)

        login_btn = Button(frame, text="Login", command=self.login, font=("Arial", 20, "bold"),
                           bg="darkblue", fg="white", cursor="hand2")
        login_btn.pack(pady=20)

        register_btn = Button(frame, text="New User? Register Here", command=self.register_window,
                              font=("Arial", 12), bg="lightblue", fg="black", cursor="hand2")
        register_btn.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", "Login Successful")
                self.open_main_window()
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error: {str(e)}")
        finally:
            if conn.is_connected():
                conn.close()

    def open_main_window(self):
        self.root.destroy()
        root = Tk()
        app = FACE_RECOGNITION(root)
        root.mainloop()

    def register_window(self):
        self.new_window = Toplevel(self.root)
        Register(self.new_window)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x600+450+150")

        Label(self.root, text="Register Here", font=("Arial", 25, "bold"), fg="darkgreen").pack(pady=20)

        Label(self.root, text="Username", font=("Arial", 18)).pack(pady=10)
        self.username_entry = Entry(self.root, font=("Arial", 15))
        self.username_entry.pack(pady=5)

        Label(self.root, text="Password", font=("Arial", 18)).pack(pady=10)
        self.password_entry = Entry(self.root, font=("Arial", 15), show='*')
        self.password_entry.pack(pady=5)

        Label(self.root, text="Email", font=("Arial", 18)).pack(pady=10)
        self.email_entry = Entry(self.root, font=("Arial", 15))
        self.email_entry.pack(pady=5)

        Label(self.root, text="Phone", font=("Arial", 18)).pack(pady=10)
        self.phone_entry = Entry(self.root, font=("Arial", 15))
        self.phone_entry.pack(pady=5)

        register_btn = Button(self.root, text="Register", command=self.register_user, font=("Arial", 20, "bold"),
                              bg="green", fg="white")
        register_btn.pack(pady=20)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if username == "" or password == "" or email == "" or phone == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email, phone) VALUES (%s, %s, %s, %s)",
                           (username, password, email, phone))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")
        finally:
            if conn.is_connected():
                conn.close()

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
