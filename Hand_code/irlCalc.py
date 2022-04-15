import cv2
import mediapipe as mp
# import os
import keyboard

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

#folderPath = "../imgs_fingers"
#myList = os.listdir(folderPath)

plus_img = cv2.imread('..\images\plus8c.png', 1)
minus_img = cv2.imread('..\images\minus4.jpg', 1)
equal_img = cv2.imread('..\images\equal2.jpg', 1)
reset_img = cv2.imread('..\images\\reset2.jpg', 1)

plus_img = cv2.cvtColor(plus_img, cv2.COLOR_BGR2GRAY)
minus_img = cv2.cvtColor(minus_img, cv2.COLOR_BGR2GRAY)
equal_img = cv2.cvtColor(equal_img, cv2.COLOR_BGR2GRAY)
reset_img = cv2.cvtColor(reset_img, cv2.COLOR_BGR2GRAY)

h, w = plus_img.shape
h2, w2 = minus_img.shape
h3, w3 = equal_img.shape
h4, w4 = equal_img.shape

threshold = 0.6

SUMA = 0
K = 0

#HandLandmark.

def right_hand(handMark, thumb): #right hand
    num_Hands = []
    middle_finger = 0

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

    #if num and middle_finger == 1:
        #return 'middle_finger'

    #cv2.putText(img, f'Right hand: {int(num)}', (400, 50), cv2.FONT_ITALIC, 1, 255, 1)
    #print(num)
    return num




def left_hand(handMark, thumb): #left hand
    num_Hands = []
    middle_finger = 0

    if thumb['HandLandmark.THUMB_TIP'] < thumb['HandLandmark.THUMB_IP']:
        num_Hands.append(1)
        #print("thumbbb lefttt")

    if handMark['HandLandmark.INDEX_FINGER_TIP'] < handMark['HandLandmark.INDEX_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.MIDDLE_FINGER_TIP'] < handMark['HandLandmark.MIDDLE_FINGER_PIP']:
        num_Hands.append(1)
        middle_finger = 1

    if handMark['HandLandmark.RING_FINGER_TIP'] < handMark['HandLandmark.RING_FINGER_PIP']:
        num_Hands.append(1)

    if handMark['HandLandmark.PINKY_TIP'] < handMark['HandLandmark.PINKY_PIP']:
        num_Hands.append(1)

    #print(num_Hands)

    num = num_Hands.count(1)

    #if num and middle_finger == 1:
        #return 'middle_finger'

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

listFin = [0, 0]
symbol = '?'

running = True

while True:

    with mp_hands.Hands(static_image_mode=True, max_num_hands=6) as hands:
        # img settings

        success, img = cap.read()
        # print(success)
        img = cv2.flip(img, 1)

        color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(color)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.resize(img, (0, 0), fx=3, fy=2.1)

        height, width, channel = img.shape
        screen = height, width

        result_plus = cv2.matchTemplate(img_gray, plus_img, cv2.TM_CCOEFF_NORMED)
        min_val_plus, max_val_plus, min_loc_plus, max_loc_plus = cv2.minMaxLoc(result_plus)

        result_minus = cv2.matchTemplate(img_gray, minus_img, cv2.TM_CCOEFF_NORMED)
        min_val_minus, max_val_minus, min_loc_minus, max_loc_minus = cv2.minMaxLoc(result_minus)

        result_equal = cv2.matchTemplate(img_gray, equal_img, cv2.TM_CCOEFF_NORMED)
        min_val_equal, max_val_equal, min_loc_equal, max_loc_equal = cv2.minMaxLoc(result_equal)

        result_reset = cv2.matchTemplate(img_gray, reset_img, cv2.TM_CCOEFF_NORMED)
        min_val_reset, max_val_reset, min_loc_reset, max_loc_reset = cv2.minMaxLoc(result_reset)

        img = cv2.rectangle(img, (1600, 0), (width, height), (156, 143, 233), -1)

        cv2.putText(img, f'- {int(listFin[0])} -', (1650, 100), cv2.FONT_ITALIC, 2, 255, 3)  # pyrvo chislo
        cv2.putText(img, f'- {symbol} -', (1650, 300), cv2.FONT_ITALIC, 2, 255, 3)  # symbol
        cv2.putText(img, f'- {int(listFin[1])} -', (1650, 500), cv2.FONT_ITALIC, 2, 255, 3)  # vtoro chislo

        if K == -1:
            cv2.putText(img, f'Equal = {SUMA}', (800, 100), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)  # sum

        if results.multi_hand_landmarks:
            #print(results.multi_hand_landmarks)
            handsType = []
            for hand in results.multi_handedness:
                #print(results.multi_handedness)
                # print(hand)
                # print(hand.classification)
                # print(hand.classification[0])
                hType = hand.classification[0].label
                handsType.append(hType)

            #print(handsType)

            for i in range(0, len(handsType)):
                if handsType[i] == 'Left':
                    handsType[i] = 'Right'
                    continue

                elif handsType[i] == 'Right':
                    handsType[i] = 'Left'

            #print("-----", handsType)

            for handLandmarks in results.multi_hand_landmarks:

                for lm in handLandmarks.landmark:
                    cx, cy = int(lm.x * width), int(lm.y * height)
                mp_draw.draw_landmarks(img, handLandmarks, mp_hands.HAND_CONNECTIONS,
                                        mp_draw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4), # connecting lines
                                        mp_draw.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2) # circle
                                       )

                for point in mp_hands.HandLandmark:

                    normalizedLandmark = handLandmarks.landmark[point]
                    #print(normalizedLandmark)

                    normCoords = normalizedLandmark.x, normalizedLandmark.y
                    pixelCoords = tuple(round(coord * dimension) for coord, dimension in zip(normCoords, screen))

                    x, y = sorted(pixelCoords)

                    #print(point)

                    if str(point) in long_fingers:
                        long_fingers[str(point)] = y

                    if str(point) in thumb:
                        thumb[str(point)] = x


                numFingers = 0

                for i in range(0, len(handsType)):
                    if handsType[i] == 'Right':
                        numFingers += right_hand(long_fingers, thumb)

                    elif handsType[i] == 'Left':
                        numFingers += left_hand(long_fingers, thumb)

                    #print(numFingers)

            if K == 0:
                listFin[0] = numFingers

            elif K == 1:
                listFin[1] = numFingers
                symbol = '+'
                SUMA = sum(listFin)

            elif K == 2:
                listFin[1] = numFingers
                symbol = '-'
                SUMA = listFin[0] - listFin[1]
                #if SUMA < 0:
                    #SUMA = ':('

    if keyboard.is_pressed('+') or max_val_plus >= threshold:
        K = 1
        #top_left = max_loc_plus
        #cv2.rectangle(img, top_left, (top_left[0] + w, top_left[1] + h), (0, 128, 0), 1)

    if keyboard.is_pressed('Enter') or max_val_equal >= threshold:
        K = -1

    if keyboard.is_pressed('-') or max_val_minus >= threshold:
        K = 2

    if keyboard.is_pressed('r') or max_val_reset >= threshold:
        K = 0
        listFin = [0, 0]
        symbol = '?'


                    #print(all_hand_landmarks)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''

'''