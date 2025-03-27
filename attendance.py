from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import StringVar
import os
from tkinter import filedialog
import mysql.connector




import csv


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.mydata=[]
        self.var_attendance_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

        # Load and resize images
        self.photoimg1 = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\1.jpg", (500, 130))
        self.photoimg2 = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\2.jpeg", (500, 130))
        self.photoimg3 = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\3.jpeg",(500, 130))

        self.photoimg_bg = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\dev.png", (1530, 710))

        # Display header images if loaded successfully
        if self.photoimg1:
            Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        if self.photoimg2:
            Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
        if self.photoimg3:
            Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=530, height=130)

        # Display background image
        if self.photoimg_bg:
            bg_img = Label(self.root, image=self.photoimg_bg)
            bg_img.place(x=0, y=130, width=1530, height=710)

        # Title label
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        left_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"), fg="black", bg="white")
        left_frame.place(x=10, y=180, width=650, height=500)

        # Labels and Entry fields with StringVar() bindings
        
        

        Label(left_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.txt_name = Entry(left_frame, font=("times new roman", 12, "bold"), width=20, textvariable=self.var_name)
        self.txt_name.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        Label(left_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        self.txt_roll = Entry(left_frame, font=("times new roman", 12, "bold"), width=20, textvariable=self.var_roll)
        self.txt_roll.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(left_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        self.txt_dept = Entry(left_frame, font=("times new roman", 12, "bold"), width=20, textvariable=self.var_dept)
        self.txt_dept.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(left_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.txt_time = Entry(left_frame, font=("times new roman", 12, "bold"), width=20, textvariable=self.var_time)
        self.txt_time.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(left_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        self.txt_date = Entry(left_frame, font=("times new roman", 12, "bold"), width=20, textvariable=self.var_date)
        self.txt_date.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(left_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.combo_attendance = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=18, state="readonly", textvariable=self.var_status)
        self.combo_attendance["values"] = ("Status", "Present", "Absent")
        self.combo_attendance.current(0)
        self.combo_attendance.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        button_frame = Frame(left_frame, bg="white")
        button_frame.place(x=10, y=400, width=630, height=70)

        Button(button_frame, text="Import CSV",command=self.importCsv, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=13).grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Export CSV",command=self.exportCsv, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=13).grid(row=0, column=1, padx=10, pady=10)
        Button(button_frame, text="Update", command=self.update,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=13).grid(row=0, column=2, padx=10, pady=10)
        Button(button_frame, text="Reset", command=self.reset_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=13).grid(row=0, column=3, padx=10, pady=10)


        # Right frame: Attendance Details
        right_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"), fg="black", bg="white")
        right_frame.place(x=670, y=180, width=650, height=500)

        # Scrollable Table
        scroll_x = Scrollbar(right_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(right_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(right_frame, columns=(  "name","roll", "dept", "time", "date", "status"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        # Set the headings and define the width of each column
        
       
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("roll", text="Roll")
        self.attendance_table.heading("dept", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("status", text="Attendance Status")
        self.attendance_table["show"] = "headings"

        # Define each column width to ensure headers are visible
        
        
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("dept", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("status", width=150)

        self.attendance_table.pack(fill=BOTH, expand=1)

        # Bind the get_cursor function to capture selected row
        self.attendance_table.bind("<ButtonRelease-1>", self.get_cursor)
    def get_cursor(self, event):
        cursor_row = self.attendance_table.focus()
        contents = self.attendance_table.item(cursor_row)
        row = contents["values"]

        if row:  # Ensure row is not empty before accessing
            self.var_name.set(row[0])
            self.var_roll.set(row[1])
            self.var_dept.set(row[2])
            self.var_time.set(row[3])
            self.var_date.set(row[4])
            self.var_status.set(row[5])




    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image {path}: {e}")
            return None
    #+++++++++++++++fetch data+++++++++++++++++++++
    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for row in rows:
            self.attendance_table.insert("", END, values=row)

    def importCsv(self):
        self.mydata.clear()  # Clear existing data before importing
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Open CSV", 
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")]
        )
        if fln:  # Check if file is selected
            try:
                with open(fln, newline='') as myfile:
                    csvread = csv.reader(myfile, delimiter=",")
                    for row in csvread:
                        self.mydata.append(row)
                    self.fetchData(self.mydata)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading CSV file: {e}", parent=self.root)

    def exportCsv(self):
        try:
            if len(self.mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(), title="Save CSV",
                filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
                defaultextension=".csv"
            )
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for row in self.mydata:
                        exp_write.writerow(row)
                messagebox.showinfo("Data Export", f"Data has been exported to {fln}", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error exporting data: {e}", parent=self.root)
    
    def update(self):
        
        
        name = self.var_name.get()
        roll = self.var_roll.get()
        dept = self.var_dept.get()
        time = self.var_time.get()
        date = self.var_date.get()
        status = self.var_status.get()
        status = self.var_status.get()

    # Ensure all fields are filled out
        if  not roll or not name or not dept or not time or not date or status == "Status":
            messagebox.showerror("Error", "All fields must be filled out!")
            return

    
    # Database connection and update operation
        try:
        # Use 'with' statements to ensure resources are managed properly
            with mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='face'
            ) as conn:
                with conn.cursor() as cursor:
                # Update query
                    query = '''UPDATE attendance
                           SET  name = %s, dept = %s, time = %s, date = %s, status = %s
                           WHERE roll = %s'''

                # Execute the query with the provided values
                    cursor.execute(query, ( name, dept, time, date, status,roll ))

                # Commit the changes
                    conn.commit()

        # Success message
            messagebox.showinfo("Success", "Attendance updated successfully!")

        except mysql.connector.Error as e:
        # Handle specific database errors
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        except Exception as e:
        # Handle any other exceptions
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")



    def reset_data(self):
    # Reset all the variables to their default empty values
        
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Status")  # Set to a default placeholder if applicable



if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()