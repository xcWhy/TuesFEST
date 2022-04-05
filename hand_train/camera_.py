import cv2
import time
import os
import uuid

IMAGES_PATH = 'C:\\Users\\eli\\Desktop\\tets\\collected_imgs\\'

labels = ['plus', 'minus']
number_imgs = 15

for label in labels:
    #!mkdir -p {'C:\\Users\\eli\\Desktop\\tets\\collected_imgs\\'+label}
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for img_num in range(0, number_imgs):
        ret, frame = cap.read()
        #print(img_name)
        if ret:
            img_name = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(img_name, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
