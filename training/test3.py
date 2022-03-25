import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #frame - img, ret - tell you if the video capture works
    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #if we press q it will stop and it will break
        break

cap.release() #osvobojdavame kamerata
cv2.destroyAllWindows()