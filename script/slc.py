from pywinauto.application import Application
import pyperclip
import pyautogui
import sys
import time

# make a function that gets information from the user

def run(region, user):

    print(region, user, flush=True)
    print("Running", flush=True)
    # foucs on the window SLC Checker - Reborn
    pyautogui.getWindowsWithTitle("SLC Checker - Reborn")[0].maximize()

    # add user to the clipboard
    pyperclip.copy(user)

    # press file button and then Load accounts from clipboard
    # check where to click

    print("clicking on file button", flush=True)


    file = pyautogui.locateOnScreen('/images/fileButton.JPG',
            confidence=0.6
    )

    print(file, flush=True)

    pyautogui.moveTo(file)
    pyautogui.mouseDown()
    pyautogui.click(file)

    time.sleep(1)

    pyautogui.mouseUp()

    print("clicking on load accounts from clipboard", flush=True)

    time.sleep(1)

    load = pyautogui.locateOnScreen('/images/clipboard.png',
            confidence=0.5
    )
    
    pyautogui.moveTo(load)
    pyautogui.mouseDown()
    pyautogui.click(load)

    time.sleep(1)   
    pyautogui.mouseUp()     


run(sys.argv[1], sys.argv[2])


    

    

