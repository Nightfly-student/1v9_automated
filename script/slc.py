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


    try :
        file = pyautogui.locateOnScreen('fileButton.JPG',
            confidence=0.6,
            minSearchTime=5
        )
    except Exception as e:
        print(e, flush=True)
        return "Could not find file button"

    print(file, flush=True)

    pyautogui.moveTo(file, duration=1)
    pyautogui.mouseDown()
    pyautogui.click(file)

    time.sleep(1)
    

    print("clicking on load accounts from clipboard", flush=True)

    time.sleep(1)

    load = pyautogui.locateOnScreen('clipboard.png',
            confidence=0.5,
            minSearchTime=5
    )
    
    pyautogui.moveTo(load, duration=1)
    pyautogui.mouseDown()
    pyautogui.click(load)

    time.sleep(1)   
    pyautogui.mouseUp()     


run(sys.argv[1], sys.argv[2])


    

    

