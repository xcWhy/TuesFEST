import numpy as np
import cv2

pluses_img = cv2.imread('../imgs_fingers/pluses.jpg', 0)
plusche_img = cv2.imread('../imgs_fingers/plusche.jpg', 0)

h, w = plusche_img.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:

    img2 = pluses_img.copy()

    result = cv2.matchTemplate(img2, plusche_img, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = min_loc

    bottom_right = (location[0] + w, location[1] + h)

    cv2.rectangle(img2, location, bottom_right, (0, 255, 0), 5) #255 - black for short

    while True:


    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()