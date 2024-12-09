from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load and resize images with specific dimensions
        self.photoimg1 = self.load_image(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\face1.jpeg", (500, 130))
        self.photoimg2 = self.load_image(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\face2.jpeg", (500, 130))
        self.photoimg3 = self.load_image(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\face 3.jpeg", (530, 130))
        self.photoimg_bg = self.load_image(r"C:\Users\Uday Bolla\OneDrive\Desktop\images\images\main2.jpg", (1530, 710))

        # Display header images
        if self.photoimg1:
            Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        if self.photoimg2:
            Label(self.root, image=self.photoimg2).place(x=500, y=0, width=500, height=130)
        if self.photoimg3:
            Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=530, height=130)

        # Display background image
        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title label and button
        title_lbl = Button(bg_img, text="TRAIN DATA SET", command=self.train_classifier, cursor="hand2", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image at {path}\n{str(e)}")
            return None

    def train_classifier(self):
        data_dir = "data"
        
        # Check if the data directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "No images found in the 'data' folder.")
            return
        
        # Get all images in the data directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]

        faces = []
        ids = []

        # Loop through each image in the directory
        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert image to grayscale
                imageNp = np.array(img, 'uint8')  # Convert image to NumPy array
                
                # Ensure file has a valid naming convention
                filename = os.path.split(image)[1]
                if filename.count('.') < 2:
                    raise ValueError(f"Invalid filename format: {filename}")
                
                id = int(filename.split('.')[1])  # Extract ID from filename

                faces.append(imageNp)
                ids.append(id)

                # Optional: Show the image being trained
                cv2.imshow("Training", imageNp)
                cv2.waitKey(10)

            except Exception as e:
                messagebox.showwarning("Warning", f"Skipping image {image}\n{str(e)}")
                continue
        
        if len(faces) == 0:
            messagebox.showerror("Error", "No valid images found for training.")
            return

        ids = np.array(ids)

        try:
            # Train the classifier using LBPH
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)

            # Save the trained classifier to a file
            clf.write("classifier.xml")
            cv2.destroyAllWindows()

            # Show a success message
            messagebox.showinfo("Result", "Training datasets completed!!")
        except Exception as e:
            messagebox.showerror("Error", f"Error during training: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
