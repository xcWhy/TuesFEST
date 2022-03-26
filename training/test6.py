import numpy as np
import cv2

soccer_img = cv2.imread('../images/soccer.jpg', 0)
ball_img = cv2.imread('../images/ball.jpg', 0)
shoe_img = cv2.imread('../images/shoe.jpg', 0)

print(soccer_img)
h, w = shoe_img.shape
h1, w1 = ball_img.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = soccer_img.copy()

    result = cv2.matchTemplate(img2, shoe_img, method)
    result1 = cv2.matchTemplate(img2, ball_img, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
        location1 = min_loc1
    else:
        location = max_loc
        location1 = max_loc1

    bottom_right = (location[0] + w, location[1] + h)
    bottom_right1 = (location1[0] + w1, location1[1] + h1)

    cv2.rectangle(img2, location, bottom_right, 255, 5) #255 - black for short
    cv2.rectangle(img2, location1, bottom_right1, 255, 5)

    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()