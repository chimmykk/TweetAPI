import subprocess
import time
import pyautogui

def automate_chatbot():
    subprocess.Popen(r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe')

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

    # Type the first message: "what is your name"
    pyautogui.typewrite("what is your name")

    # Press "Enter" key to send the first message
    pyautogui.press('enter')

    time.sleep(2)

    # Type the second message: "what is your favorite food"
    pyautogui.typewrite("what is your favorite food")

    # Press "Enter" key to send the second message
    pyautogui.press('enter')

automate_chatbot()
