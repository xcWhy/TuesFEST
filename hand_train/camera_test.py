import cv2

template = cv2.imread('C:\\Users\\eli\\Desktop\\tets\\imgs_fingers\\plus8.jpg')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
h, w = template.shape

#print(h)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    img = cv2.flip(img, 1)
    #print(ret)
    #print(img)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF)

    if len(result):

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        location = max_loc

        cv2.rectangle(img, location, (location[0] + w, location[1] + h), (0, 128, 0), 1)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
