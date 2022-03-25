import cv2
import random

img = cv2.imread('../images/forTheEmail.jpg', 1)

#print(img)
#print(img.shape)
#print(img[257][400])

tag = img[100:300, 400:450] #row from 500 to 700, cols 600 to 900
img[200:400, 300:350] = tag

'''
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
'''

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()