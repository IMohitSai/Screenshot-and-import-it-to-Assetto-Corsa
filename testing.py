import pyautogui
from datetime import datetime

# Set the screenshot filename format
filename_format = "screenshot_{}"

while True:
    # Take a screenshot
    image = pyautogui.screenshot()

    # Get the current timestamp to use in the filename
    now = datetime.now()
    formatted_timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")

    # Save the screenshot with the current timestamp as part of its name
    image.save(f"{filename_format.format(formatted_timestamp)}.png")

#this is still a WIP and will be improved upon
