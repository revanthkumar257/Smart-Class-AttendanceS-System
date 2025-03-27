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
        self.photoimg1 = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\face1.jpeg", (500, 130))
        self.photoimg2 = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\face2.jpeg", (500, 130))
        self.photoimg3 = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\face 3.jpeg", (530, 130))
        self.photoimg_bg = self.load_image(r"D:\smart-class-attendance\smart-class-attendance-\images\images\main2.jpg", (1530, 710))

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
        title_lbl = Button(bg_img, text="TRAIN DATA SET", command=self.train_classifier, cursor="hand2",
                           font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

    def load_image(self, path, size):
        """ Load and resize an image """
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image at {path}\n{str(e)}")
            return None

    def train_classifier(self):
        """ Train the face recognition model using images from the 'data' folder """
        data_dir = r"D:\smart-class-attendance\smart-class-attendance-\data"

        # Check if the folder exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Folder '{data_dir}' not found. Please check the path.")
            return

        # Get all image paths
        image_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith((".jpg", ".jpeg", ".png"))]

        if len(image_paths) == 0:
            messagebox.showerror("Error", "No images found in the 'data' folder. Capture images first.")
            return

        faces = []
        ids = []

        # Loop through each image
        for image_path in image_paths:
            try:
                img = cv2.imread(image_path)
                
                if img is None:
                    raise ValueError(f"Could not read image {image_path}")

                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
                gray_img = cv2.resize(gray_img, (200, 200))  # Resize for consistency

                filename = os.path.basename(image_path)  # Get filename

                # Extract user ID from filename (Expected format: "User.ID.Number.jpg")
                filename_parts = filename.split('.')
                if len(filename_parts) < 3 or not filename_parts[1].isdigit():
                    messagebox.showwarning("Warning", f"Skipping image {image_path}. Invalid filename format.")
                    continue

                id = int(filename_parts[1])  # Extract ID from filename
                faces.append(gray_img)
                ids.append(id)

                # Show image while training (Optional)
                try:
                    cv2.imshow("Training", gray_img)
                    cv2.waitKey(10)
                except:
                    pass  # Ignore errors in headless environments

            except Exception as e:
                messagebox.showwarning("Warning", f"Skipping image {image_path}\n{str(e)}")
                continue

        cv2.destroyAllWindows()

        if len(faces) == 0:
            messagebox.showerror("Error", "No valid images found for training.")
            return

        ids = np.array(ids)

        try:
            # Ensure OpenCV has face recognition module
            if not hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
                messagebox.showerror("Error", "OpenCV Face Recognizer not available. Install opencv-contrib-python.")
                return

            # Train the classifier
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)

            # Save the trained model
            model_path = os.path.join(data_dir, "trained_model.xml")
            clf.write(model_path)

            messagebox.showinfo("Success", "Training completed successfully! Model saved.")
        except Exception as e:
            messagebox.showerror("Error", f"Training error: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
