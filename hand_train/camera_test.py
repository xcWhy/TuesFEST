'''
import time
import cv2
import numpy as np


# initialize the camera and grab a reference to the raw camera capture
cap = cv2.VideoCapture(0)

template = cv2.imread('C:\\Users\\eli\\Desktop\\tets\\imgs_fingers\\plus2.jpg', 0)

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in cap:
    # grab the raw NumPy array representing the image,
    # then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # we do something here
    # we get the image or something then run some matching
    # if we get a match, we draw a square on it or something
    img_rgb = image

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    template = cv2.imread("mario_coin.png", 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8

    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, (pt[1]. pt[0]), (pt[1] + w, pt[0] + h),
                      (0,0,255), 2)

    # show the frame
    cv2.imshow("Frame", img_rgb)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    #rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
'''

import cv2
import numpy as np
import time

#name = 'plus2.jpg'
template = cv2.imread('C:\\Users\\eli\\Desktop\\tets\\imgs_fingers\\plus4.jpg', 0)
face_w, face_h = template.shape[::-1]

cv2.namedWindow('image')

cap = cv2.VideoCapture(0)

threshold = 0.8
ret = True

while ret:
    ret, img = cap.read()

    #flip the image  ! optional
    #img = cv2.flip(img,1)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCORR)

    if len(res):
        #print(res)
        #time.sleep(0.1)
        location = np.where(res >= threshold)
        #print(location)
        for pt in zip(*location[::-1]):
            #puting  rectangle on recognized erea
            cv2.rectangle(img, pt, (pt[0] + face_w, pt[1] + face_h), (0,0,255), 2)

    #print(res)
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
