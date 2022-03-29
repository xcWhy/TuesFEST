import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

all_hand_landmarks = {
    "HandLandmark.WRIST": 0,
    "HandLandmark.THUMB_CMC": 0,
    "HandLandmark.THUMB_MCP": 0,
    "HandLandmark.THUMB_IP": 0,
    "HandLandmark.THUMB_TIP": 0,
    "HandLandmark.INDEX_FINGER_MCP": 0,
    "HandLandmark.INDEX_FINGER_PIP": 0,
    "HandLandmark.INDEX_FINGER_DIP": 0,
    "HandLandmark.INDEX_FINGER_TIP": 0,
    "HandLandmark.MIDDLE_FINGER_MCP": 0,
    "HandLandmark.MIDDLE_FINGER_PIP": 0,
    "HandLandmark.MIDDLE_FINGER_DIP": 0,
    "HandLandmark.MIDDLE_FINGER_TIP": 0,
    "HandLandmark.RING_FINGER_MCP": 0,
    "HandLandmark.RING_FINGER_PIP": 0,
    "HandLandmark.RING_FINGER_DIP": 0,
    "HandLandmark.RING_FINGER_TIP": 0,
    "HandLandmark.PINKY_MCP": 0,
    "HandLandmark.PINKY_PIP": 0,
    "HandLandmark.PINKY_DIP": 0,
    "HandLandmark.PINKY_TIP": 0
}

def hand_sign(coords, landmarks_list, point):
    #print(landmarks_list)
    #print(coords)
    sorted(coords)
    x, y = coords
    #print(y)

    #if point == landmarks_list[8]:

def to_pixel_coords():
    pass


while True:
    success, img = cap.read()
    #print(success)
    landmarks_list = []

    with mp_hands.Hands(static_image_mode=True, max_num_hands=4) as hands:
        color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(color)
        height, width, channel = img.shape
        y_coord = []
        i = 0



    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            for point in mp_hands.HandLandmark:

                normalizedLandmark = handLandmarks.landmark[point]
                print(normalizedLandmark)
                pixelCoordinatesLandmark = mp_draw._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                        normalizedLandmark.y, height,
                                                                                        width)
                print(point)
                print(pixelCoordinatesLandmark)
                myTuple = pixelCoordinatesLandmark
                print(sorted(pixelCoordinatesLandmark)) #problemo ne moje da sortira none

                print(str(point))

                x, y = sorted(pixelCoordinatesLandmark)

                if str(point) in all_hand_landmarks:
                    pass
                    all_hand_landmarks[point] = y
                    print(all_hand_landmarks)

                hand_sign(pixelCoordinatesLandmark, landmarks_list, point)
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