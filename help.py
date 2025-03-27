from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed size for now
        self.root.title("Face Recognition System")
        
        # Title Label: Centered at the top
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=2, y=0, width=1530, height=50)
        
        # Load and resize the background image
        img_top = Image.open(r"D:\smart-class-attendance\smart-class-attendance-\images\images\help.jpeg")
        img_top = img_top.resize((1530, 740), Image.LANCZOS)  # Adjust height to 740
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Place the background image below the title label
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=740)  # Set height to 740
        
        # Developer information text
        dev_label = Label(f_lbl, text="EMAIL: revanthyadav05@gmail.com", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.place(x=400, y=200)

if __name__ == "__main__":
    root = Tk()
    
    obj = Help(root)
    root.mainloop()
