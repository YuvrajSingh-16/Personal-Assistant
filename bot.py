from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
import webbrowser
import sys

class Coordinates:
    replayBtn = (684, 400)  # Chrome dino game (305, 384)
    dino = (153, 410)       # Chrome dino game (187, 318)
    # 174 x-coordinates for rectangle area
    # 342 y-coordinates for small tree


def restartGame():
    pyautogui.click(Coordinates.replayBtn)


def pressSpace():
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp("space")
    pyautogui.keyDown("down")


def imageGrab():
    box = (Coordinates.dino[0], Coordinates.dino[1], Coordinates.dino[0] + 248, Coordinates.dino[1] + 30)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = np.array(greyImage.getcolors())
    return a.sum()


def PreDino():
    webbrowser.open("www.google.com")
    time.sleep(2)
    pyautogui.click(645, 53)
    pyautogui.typewrite("chrome://dino")
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


def main():
    PreDino()
    pyautogui.click(670, 316)
    time.sleep(2)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

    restartGame()

    while True:
        #imageGrab()
        if imageGrab() != 7695:   # 4755 on extended screen and 7755 or 7695 on single screen
            pressSpace()
            time.sleep(.1)
        
        if pyautogui.locateAllOnScreen("restartButton.png") != None:
            break


if __name__ == "__main__":
    main()
     