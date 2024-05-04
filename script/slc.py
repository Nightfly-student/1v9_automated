from pywinauto.application import Application
import pyperclip
import sys


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
    app.window(title_re="SLC Checker - Reborn").print_control_identifiers()


    window.file.click_input()
    window.menu_select("File->Load accounts from clipboard")

run(sys.argv[1], sys.argv[2])


    

    

