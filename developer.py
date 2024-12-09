from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Fixed size for now
        self.root.title("Face Recognition System")
        
        # Title Label: Centered at the top
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
        # Load and resize the background image
        img_top = Image.open(r"C:\Users\Uday Bolla\OneDrive\Desktop\BTP NANDINI\smart-class-attendence-system\images\images\dev.png")
        img_top = img_top.resize((1530, 745), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Place the background image below the title label
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=740)
        
        # Frame for developer info - centered in the middle of the window
        frame_width = 600
        frame_height = 350
        center_x = (self.root.winfo_screenwidth() - frame_width) // 2
        center_y = (self.root.winfo_screenheight() - frame_height) // 2
        
        # Developer info frame
        main_frame = Frame(f_lbl, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)
        
        # Load and resize the developer's image
        img_dev = Image.open(r"C:\Users\Uday Bolla\Downloads\WhatsApp Image 2024-11-23 at 19.19.44_0a185cb2.jpg")
        img_dev = img_dev.resize((150, 150), Image.LANCZOS)
        self.photoimg_dev = ImageTk.PhotoImage(img_dev)
        
        # Place the developer's image inside the frame
        img_lbl = Label(main_frame, image=self.photoimg_dev, bg="white")
        img_lbl.place(x=225, y=30, width=150, height=150)
        
        # Developer information text
        dev_label = Label(main_frame, text="Hello, my name is Nandini", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.place(x=120, y=200)
        
        dev_info = Label(main_frame, text="pre-final year student at RGIPT ", font=("times new roman", 15), fg="black", bg="white")
        dev_info.place(x=160, y=240)
        
        # Add an additional section for a description
        dev_desc = Label(main_frame, text="currently working on smart class attendence project", font=("times new roman", 15), fg="green", bg="white")
        dev_desc.place(x=130, y=270)

if __name__ == "__main__":
    root = Tk()
    root.update_idletasks()
    obj = Developer(root)
    root.mainloop()
