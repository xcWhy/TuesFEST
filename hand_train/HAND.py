import cv2
import time
import os

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "imgs_fingers"
myList = os.listdir(folderPath) #its important to be in order

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)