import subprocess
import time
import pyautogui

def automate_chatbot():
    # Open the chatbot application
    process = subprocess.Popen(r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe')

    time.sleep(2)

    # Press "Tab" key three times to navigate to the Doge option
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    # Press "Enter" key to select the Doge option
    pyautogui.press('enter')

    time.sleep(2)

    # Press "Tab" key three times to trigger three tabs again
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    time.sleep(2)

    # Type "what is your name"
    pyautogui.typewrite("what is your name")

    # Press "Enter" key to send the message
    pyautogui.press('enter')

    # Add a 2-second delay
    time.sleep(2)

    # Wait for 1 minute
    time.sleep(60)

    # Close the application
    process.terminate()

automate_chatbot()
