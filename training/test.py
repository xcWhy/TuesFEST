import cv2

img = cv2.imread('../images/forTheEmail.jpg', 1)
img = cv2.resize(img, (0, 0), fx=2, fy=2) #double the size
img = cv2.rotate(img, cv2.cv2.ROTATE_180) #rotation

#cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0) #waits infinite amount of time, (5) shte chaka 5 sec
cv2.destroyAllWindows()

'''
-1 = cv2.IMREAD_COLOR - color image without != transparency
0 = cv2.IMREAD_GRAYSCALE - grayscale mode img
1 = cv2.IMREAD_UNCHANGED - color image + transparancy
'''

