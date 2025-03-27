import cv2
import os

cascade_path = "haarcascade_frontalface_default.xml"

if not os.path.exists(cascade_path):
    print("Error: Haar cascade file not found!")
else:
    print("Success: Haar cascade file found!")
