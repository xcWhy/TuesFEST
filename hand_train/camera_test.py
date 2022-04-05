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

template = cv2.imread('C:\\Users\\eli\\Desktop\\tets\\imgs_fingers\\plus6.jpg')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
h, w = template.shape

#print(h)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    #img = cv2.flip(img,1)
    print(ret)
    print(img)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = max_loc

    cv2.rectangle(img, location, (location[0] + w, location[1] + h), (0, 128, 0), 1)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
