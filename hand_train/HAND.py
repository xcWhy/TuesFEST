import cv2
import time
import os

cap = cv2.VideoCapture(0)

folderPath = "../imgs_fingers"
myList = os.listdir(folderPath)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

pTime = 0

while True:
    success, img = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    h, w, c = overlayList[0].shape
    img[0:h, 0:w] = overlayList[0] #overlay the image

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (500, 50), cv2.FONT_ITALIC, 1, 255, 3)

    cv2.imshow('Image', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()