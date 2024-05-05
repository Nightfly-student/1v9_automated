from pywinauto.application import Application
import pyperclip
import pyautogui
import sys
import time
import cv2
from pathlib import Path

# make a function that gets information from the user

def run(region, user):
    # foucs on the window SLC Checker - Reborn
    app = Application().connect(title_re="SLC Checker - Reborn")

    # get the window

    window = app.window(title_re="SLC Checker - Reborn")

    # if no window is found, return an error message
    if not window.exists():
        return "No window found"
    
    # add user to the clipboard
    pyperclip.copy(user)

    # focus on the window
    window.set_focus()

    # press file button and then Load accounts from clipboard
    # check where to click


    moveAndClickToFile("fileButton.JPG", 2, 0.7)
    moveAndClickToFile("clipboard.png", 2, 0.8)  

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(2)

    # moveAndClickToFile("import.JPG", 3, 0.5)

    moveAndClickToFile("checkerButton.PNG", 2, 0.75) 
    moveAndClickToFile("checkerStart.PNG", 1, 0.7)

    keepGoing = True
    while keepGoing:
        time.sleep(2)
        found = waitUntilFileButton("finished.JPG")
        if found:
            keepGoing = False
        else:
            keepGoing = True

    moveAndClickToFile("toAccount.JPG", 1, 0.7) 

    pyautogui.rightClick(duration=0.5)
    time.sleep(1)

    moveAndClickToFile("copyInfo.JPG", 1, 0.7)
    moveAndClickToFileBackwards("copyFormat.JPG", 2, 0.7)
    moveAndClickToFile("exportToCSV.JPG", 1, 0.85)

    time.sleep(2)

    # do it twice to make sure it works
    for i in range(2):
        moveAndClickToFile("edit.JPG", 2, 0.7)
        moveAndClickToFile("clearAccount.JPG", 3, 0.7)
        pyautogui.press('enter')
        pyautogui.press('enter')
    
    print(pyperclip.paste(), flush=True)

    time.sleep(5)

    return pyperclip.paste()



def moveAndClickToFile (fileName, sleepTime, confidence=0.8, click=1):
    filePath = cv2.imread('script/' + fileName)

    try:
        file = pyautogui.locateCenterOnScreen(filePath,
            confidence=confidence,
        )
    except Exception as e:
        return "Could not find file button"
    
    # move first only the y axis then x axis
    pyautogui.move(0, file.y, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.move(file.x, 0, duration=1, tween=pyautogui.easeInOutQuad)

    # pyautogui.moveTo(file, duration=0.5)
    pyautogui.click(file, clicks=click, interval=0.0, button='left', duration=0.2)   

    time.sleep(sleepTime)

    return

def waitUntilFileButton (fileName):
    filePath = cv2.imread('script/' + fileName)
    
    try:
        pyautogui.locateOnScreen(filePath,
            confidence=0.65,
        )
        return True
    except Exception as e:
        return False

def moveAndClickToFileBackwards (fileName, sleepTime, confidence=0.8, click=1):
    filePath = cv2.imread('script/' + fileName)

    try:
        file = pyautogui.locateCenterOnScreen(filePath,
            confidence=confidence,
        )
    except Exception as e:
        return "Could not find file button"
    
    # move first only the y axis then x axis
    pyautogui.move(file.x, 0, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.move(0, file.y, duration=1, tween=pyautogui.easeInOutQuad)

    # pyautogui.moveTo(file, duration=0.5)
    pyautogui.click(file, clicks=click, interval=0.0, button='left', duration=0.2)   

    time.sleep(sleepTime)

    return

run(sys.argv[1], sys.argv[2])