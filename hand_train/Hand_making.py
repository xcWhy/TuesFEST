import cv2
import mediapipe as mp
import time
import os


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

folderPath = "../imgs_fingers"
myList = os.listdir(folderPath)

SUMA = 0
K = 0

#HandLandmark.

def right_hand(handMark, thumb): #right hand
    num_Hands = []

    if thumb['HandLandmark.THUMB_TIP'] > thumb['HandLandmark.THUMB_IP']:
        num_Hands.append(1)
        #print("thumbbb right")

    if handMark['HandLandmark.INDEX_FINGER_TIP'] < handMark['HandLandmark.INDEX_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.MIDDLE_FINGER_TIP'] < handMark['HandLandmark.MIDDLE_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.RING_FINGER_TIP'] < handMark['HandLandmark.RING_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.PINKY_TIP'] < handMark['HandLandmark.PINKY_PIP']:
        num_Hands.append(1)

    num = num_Hands.count(1)

    #cv2.putText(img, f'Right hand: {int(num)}', (400, 50), cv2.FONT_ITALIC, 1, 255, 1)
    #print(num)
    return num




def left_hand(handMark, thumb): #left hand
    num_Hands = []

    if thumb['HandLandmark.THUMB_TIP'] < thumb['HandLandmark.THUMB_IP']:
        num_Hands.append(1)
        #print("thumbbb lefttt")

    if handMark['HandLandmark.INDEX_FINGER_TIP'] < handMark['HandLandmark.INDEX_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.MIDDLE_FINGER_TIP'] < handMark['HandLandmark.MIDDLE_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.RING_FINGER_TIP'] < handMark['HandLandmark.RING_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.PINKY_TIP'] < handMark['HandLandmark.PINKY_PIP']:
        num_Hands.append(1)

    #print(num_Hands)

    num = num_Hands.count(1)

    #cv2.putText(img, f'Left hand: {int(num)}', (100, 50), cv2.FONT_ITALIC, 1, 255, 1)
    #print(num)
    return num


thumb = {
    "HandLandmark.THUMB_CMC": 0,  # 1
    "HandLandmark.THUMB_MCP": 0,  # 2
    "HandLandmark.THUMB_IP": 0,  # 3
    "HandLandmark.THUMB_TIP": 0,  # 4
}

long_fingers = {
    "HandLandmark.WRIST": 0,  # 0
    "HandLandmark.INDEX_FINGER_MCP": 0, #5
    "HandLandmark.INDEX_FINGER_PIP": 0, #6
    "HandLandmark.INDEX_FINGER_DIP": 0, #7
    "HandLandmark.INDEX_FINGER_TIP": 0, #8
    "HandLandmark.MIDDLE_FINGER_MCP": 0, #9
    "HandLandmark.MIDDLE_FINGER_PIP": 0, #10
    "HandLandmark.MIDDLE_FINGER_DIP": 0, #11
    "HandLandmark.MIDDLE_FINGER_TIP": 0, #12
    "HandLandmark.RING_FINGER_MCP": 0, #13
    "HandLandmark.RING_FINGER_PIP": 0, #14
    "HandLandmark.RING_FINGER_DIP": 0, #15
    "HandLandmark.RING_FINGER_TIP": 0, #16
    "HandLandmark.PINKY_MCP": 0, #17
    "HandLandmark.PINKY_PIP": 0, #18
    "HandLandmark.PINKY_DIP": 0, #19
    "HandLandmark.PINKY_TIP": 0 #20
}

listFin = [0]

with mp_hands.Hands(static_image_mode=True, max_num_hands=6) as hands:

    while True:

        success, img = cap.read()
        # print(success)
        img = cv2.flip(img, 1)

        color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(color)
        height, width, channel = img.shape
        screen = height, width


        if results.multi_hand_landmarks:
            #print(results.multi_hand_landmarks)
            handsType = []

            for hand_landmarks in results.multi_hand_landmarks:
                for lm in hand_landmarks.landmark:
                    height, width, channel = img.shape
                    cx, cy = int(lm.x * width), int(lm.y * height)
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                        mp_draw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4), #connecting lines
                                        mp_draw.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2) #circle
                                       )


            for hand in results.multi_handedness:
                #print(results.multi_handedness)
                # print(hand)
                # print(hand.classification)
                # print(hand.classification[0])
                handType = hand.classification[0].label
                handsType.append(handType)

            #print(handsType)

            for i in range(0, len(handsType)):
                if handsType[i] == 'Left':
                    handsType[i] = 'Right'
                    continue

                if handsType[i] == 'Right':
                    handsType[i] = 'Left'
                    continue

            #print("-----", handsType)

            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:

                    normalizedLandmark = handLandmarks.landmark[point]
                    #print(normalizedLandmark)

                    normCoords = normalizedLandmark.x, normalizedLandmark.y
                    pixelCoords = tuple(round(coord * dimension) for coord, dimension in zip(normCoords, screen))

                    x, y = sorted(pixelCoords)

                    #print(point)

                    if str(point) in long_fingers:
                        #print("HEY U HERE?")
                        long_fingers[str(point)] = y
                        #print(all_hand_landmarks)
                        #print(all_hand_landmarks[point])

                    if str(point) in thumb:
                        thumb[str(point)] = x


                    numFingers = 0
                    for i in range(0, len(handsType)):
                        if handsType[i] == 'Right':
                            numFingers += right_hand(long_fingers, thumb)

                        elif handsType[i] == 'Left':
                            numFingers += left_hand(long_fingers, thumb)



            if K == 0:
                listFin[0] = numFingers
                cv2.putText(img, f'Fingers: {int(listFin[0])}', (50, 50), cv2.FONT_ITALIC, 1, 255, 1)

            if K > 0:
                #print(listFin)
                cv2.putText(img, f'Fingers: {int(listFin[0])}', (50, 50), cv2.FONT_ITALIC, 1, 255, 1)
                listFin[1] = numFingers
                cv2.putText(img, f'symbol: +', (50, 100), cv2.FONT_ITALIC, 1, 255, 1)
                cv2.putText(img, f'Fingers: {int(listFin[1])}', (50, 150), cv2.FONT_ITALIC, 1, 255, 1)

            if K == -1:
                SUMA = sum(listFin)
                cv2.putText(img, f'Fingers: {int(listFin[0])}', (50, 50), cv2.FONT_ITALIC, 1, 255, 1) # pyrvo chislo
                cv2.putText(img, f'symbol: +', (50, 100), cv2.FONT_ITALIC, 1, 255, 1) # +
                cv2.putText(img, f'Fingers: {int(listFin[1])}', (50, 150), cv2.FONT_ITALIC, 1, 255, 1) #vtoro chislo
                cv2.putText(img, f'sum = {SUMA}', (50, 200), cv2.FONT_ITALIC, 1, 255, 1) #sum

            if cv2.waitKey(1) & 0xff == ord('='):
                K += 1
                listFin.append(0)
                #print(listFin)


            if cv2.waitKey(1) & 0xff == ord('z'):
                K = -1


                    #print(all_hand_landmarks)

        cv2.imshow("Camera", img)



        if cv2.waitKey(1) & 0xff == ord('-'):
            print("-")

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

'''

'''