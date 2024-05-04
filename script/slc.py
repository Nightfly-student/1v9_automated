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

    filePath = cv2.imread("script/fileButton.JPG")

# C:\Users\Administrator\1v9_automated\script\fileButton.JPG

    moveAndClickToFile("fileButton.JPG", 1)
    moveAndClickToFile("clipboard.png", 1)  
    moveAndClickToFile("import.JPG", 1)

    time.sleep(2)

    moveAndClickToFile("checkerButton.JPG", 1) 
    moveAndClickToFile("checkerStart.JPG", 1)

    waitUntilFileButton("finished.JPG")

    time.sleep(2)

    moveAndClickToFile("toAccount.JPG", 1)  
    moveAndClickToFile("copyInfo.JPG", 1)
    moveAndClickToFile("copyFormat.JPG", 1)
    moveAndClickToFile("exportToCSV.JPG", 1)

    time.sleep(2)

    # do it twice to make sure it works
    for i in range(2):
        moveAndClickToFile("edit.JPG", 1)
        moveAndClickToFile("clearAccount.JPG", 1)
        moveAndClickToFile("clearAccountAccept.JPG", 1)

    return pyperclip.paste()



def moveAndClickToFile (fileName, sleepTime):
    filePath = cv2.imread('script/' + fileName)

    try:
        file = pyautogui.locateOnScreen(filePath,
            confidence=0.7,
            minSearchTime=5
        )
    except Exception as e:
        return "Could not find file button"
    
    pyautogui.moveTo(file, duration=1)
    pyautogui.click(file)   

    time.sleep(sleepTime)

    return

def waitUntilFileButton (fileName):
    filePath = cv2.imread('script/' + fileName)

    while True:
        try:
            file = pyautogui.locateOnScreen(filePath,
                confidence=0.7,
                minSearchTime=5
            )
        except Exception as e:
            return "Could not find file button"
        
        if file:
            break

    return True

run(sys.argv[1], sys.argv[2])


    

    

