import numpy as np
import cv2


img = cv2.imread('../images/forTheEmail.jpg', 1)
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img, 100, 0.4, 10) # 100 - max corners, 0.01 - kolko tochni da sa, 10 - min razstoqnie mejdu tqh
corners = np.int0(corners) #prevtyshta gi v int

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        #color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) #size - kolko pyti iskame randoma
        cv2.line(img, corner1, corner2, (255, 0, 0), 1)


cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
cap = cv2.VideoCapture(0)
cap = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read() #frame - img, ret - tell you if the video capture works
    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #if we press q it will stop and it will break
        break

cap.release() #osvobojdavame kamerata
cv2.destroyAllWindows()
'''