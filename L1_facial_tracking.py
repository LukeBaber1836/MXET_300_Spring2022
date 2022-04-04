# OpenCV program to detect face in real time
import cv2

# Face tracker XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

size_w  = 240   # Resized image width. This is the image width in pixels
size_h = 160	# Resized image height. This is the image height in pixels

# capture frames from a camera
cap = cv2.VideoCapture(0)
cap.set(3, size_w)                       # Set width of images that will be retrived from camera
cap.set(4, size_h)                       # Set height of images that will be retrived from camera

while 1:
    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Print out X and Y cordinates for the top left corner of the box
        print(x, y)
        