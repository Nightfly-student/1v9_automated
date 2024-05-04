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


    moveAndClickToFile("fileButton.JPG", 1, 0.7)
    moveAndClickToFile("clipboard.png", 2, 0.8)  

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(2)

    # moveAndClickToFile("import.JPG", 3, 0.5)

    print("imported", flush=True)
    moveAndClickToFile("checkerButton.PNG", 0.5, 0.75) 
    print("clicked checker", flush=True)
    moveAndClickToFile("checkerStart.PNG", 1, 0.7)

    keepGoing = True
    while keepGoing:
        time.sleep(2)
        found = waitUntilFileButton("finished.JPG")
        print(found, flush=True)
        if found:
            keepGoing = False
        else:
            keepGoing = True

    moveAndClickToFile("toAccount.JPG", 1, 0.7) 

    pyautogui.rightClick(duration=0.5)
    time.sleep(1)

    moveAndClickToFile("copyInfo.JPG", 1, 0.7)
    moveAndClickToFile("copyFormat.JPG", 1, 0.7)
    moveAndClickToFile("exportToCSV.JPG", 1, 0.7)

    # time.sleep(2)

    # # do it twice to make sure it works
    # for i in range(2):
    #     moveAndClickToFile("edit.JPG", 1, 0.8)
    #     moveAndClickToFile("clearAccount.JPG", 3, 0.7)
    #     moveAndClickToFile("clearAccountAccept.JPG", 1, 0.5)

    return pyperclip.paste()



def moveAndClickToFile (fileName, sleepTime, confidence=0.8, click=1):
    filePath = cv2.imread('script/' + fileName)

    try:
        file = pyautogui.locateCenterOnScreen(filePath,
            confidence=confidence,
        )
    except Exception as e:
        print("Could not find file button", flush=True)
        return "Could not find file button"
    
    # move first only the y axis then x axis
    pyautogui.move(0, file.y, duration=0.5)
    pyautogui.move(file.x, 0, duration=0.5)
    print(file, flush=True)

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
        print("waiting for file button", flush=True)
        return True
    except Exception as e:
        print("Could not find file button", flush=True)
        return False

run(sys.argv[1], sys.argv[2])


    

    

