import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()


#HandLandmark.

def hand_sign(handMark):
    i = 0
    #print("pok----", handMark['HandLandmark.INDEX_FINGER_TIP']) #STOInostite ne se promenqt
    #print("sre----", handMark['HandLandmark.MIDDLE_FINGER_TIP'])
    if handMark['HandLandmark.INDEX_FINGER_TIP'] < handMark['HandLandmark.MIDDLE_FINGER_TIP']:
        print("YES - PRYST NAGORE------------------------------------------")
        i += 1
        print(i)

all_hand_landmarks = {
    "HandLandmark.WRIST": 0, #0
    "HandLandmark.THUMB_CMC": 0, #1
    "HandLandmark.THUMB_MCP": 0, #2
    "HandLandmark.THUMB_IP": 0, #3
    "HandLandmark.THUMB_TIP": 0, #4
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


while True:
    success, img = cap.read()
    #print(success)

    with mp_hands.Hands(static_image_mode=True, max_num_hands=4) as hands:
        color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(color)
        height, width, channel = img.shape
        screen = height, width
        y_coord = []
        i = 0



    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            for point in mp_hands.HandLandmark:

                normalizedLandmark = handLandmarks.landmark[point]
                #print(normalizedLandmark)

                normCoords = normalizedLandmark.x, normalizedLandmark.y
                pixelCoords = tuple(round(coord * dimension) for coord, dimension in zip(normCoords, screen))

                x, y = sorted(pixelCoords)

                #print(point)

                if str(point) in all_hand_landmarks:
                    #print("HEY U HERE?")
                    all_hand_landmarks[str(point)] = y
                    #print(all_hand_landmarks)
                    #print(all_hand_landmarks[point])

                hand_sign(all_hand_landmarks)
                #print(all_hand_landmarks)



    if results.multi_hand_landmarks:
        for hand_dotes in results.multi_hand_landmarks:
            for lm in hand_dotes.landmark:
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
            mp_draw.draw_landmarks(img, hand_dotes, mp_hands.HAND_CONNECTIONS)



    cv2.imshow("Camera", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''

'''