import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #frame - img, ret - tell you if the video capture works
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.rectangle(frame, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(frame, (300, 300), 60, (0, 0, 255), -1) #kogato e -1, zapylva figurata s cveta izcqlo, 60 - radius
    font = cv2.FONT_ITALIC
    img = cv2.putText(frame, 'Show me your hand! :D', (10, height - 10), font, 1, (0, 0, 0), 5, cv2.LINE_AA) #for better text cv2.LINE_AA; 4 = scale of font

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #if we press q it will stop and it will break
        break

cap.release() #osvobojdavame kamerata
cv2.destroyAllWindows()

'''
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) #where to put it (frame), coordinates - top left corner 0,0, coords from start to end, color, thickness
    img2 = cv2.line(frame, (width, 0), (0, height), (255, 0, 0), 10) #where to put it (frame), coordinates - top left corner 0,0, coords from start to end, color, thickness
'''