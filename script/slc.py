from pywinauto.application import Application
import pyperclip
import pyautogui
import sys
import time
import cv2
from pathlib import Path
print(Path.cwd())

# make a function that gets information from the user

def run(region, user):

    print(region, user, flush=True)
    print("Running", flush=True)
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

    print("clicking on file button", flush=True)

    filePath = cv2.imread("script/fileButton.JPG")

    print(filePath, flush=True)

# C:\Users\Administrator\1v9_automated\script\fileButton.JPG

    moveAndClickToFile("fileButton.JPG", 1)
    moveAndClickToFile("clipboard.png", 1)   


def moveAndClickToFile (fileName, sleepTime):
    filePath = cv2.imread('script/' + fileName)

    try:
        file = pyautogui.locateOnScreen(filePath,
            confidence=0.6,
            minSearchTime=5
        )
    except Exception as e:
        print(e, flush=True)
        return "Could not find file button"
    
    print(file, flush=True)

    pyautogui.moveTo(file, duration=1)
    pyautogui.click(file)   

    time.sleep(sleepTime)

    return



run(sys.argv[1], sys.argv[2])


    

    

