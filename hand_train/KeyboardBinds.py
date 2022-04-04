import cv2
import keyboard

def KeyBinds(K, listFin, numFingers, SUMA, img):

    if keyboard.is_pressed('+'):
        K = 1

    if keyboard.is_pressed('='):
        K = -1

    if keyboard.is_pressed('-'):
        K = 2

    if keyboard.is_pressed('r'):
        K = 0
        listFin = [0, 0]

    return K