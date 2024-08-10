import pyautogui
import subprocess
import time

import ctypes
import subprocess
import sys
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Run your code here
    subprocess.Popen(
        r'"C:\Program Files\BlueStacks_msi5\HD-Player.exe" --instance Nougat64 --cmd launchAppWithBsx --package '
        r'"com.google.android.apps.maps" --source desktop_shortcut')

else:
    # Re-run the script with admin privileges
    print("Re-running script with admin privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# Step 2: Wait for the app to open
print('sleeping for 15 sec')
time.sleep(11)  # Wait 5 seconds for the app to open

# Option 2: If you have an image of the button
# Make sure to have an image of the button stored as 'button.png'
button_location = pyautogui.locateCenterOnScreen("button.png")
print(button_location)

pix = pyautogui.pixel(x=button_location.x, y=button_location.y)
print(f'pixel: {pix}')
if button_location is not None:
    try:
        pyautogui.click(button_location)
    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
else:
    print("Button not found!")

# Step 4: Take a screenshot
time.sleep(3)  # Wait 2 seconds after clicking (adjust as needed)
screenshot = pyautogui.screenshot()

# Step 5: Save the screenshot
screenshot.save(f"screenshot_{dt_string}.png")

print("Screenshot taken and saved as 'screenshot.png'")
