import subprocess
import time
import pyautogui
import os
import socket

"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'rilsos'
token = 'oauth:wb7ph6zjttttvdtk9x3uz27vy8umdi'
channel = 'dylansafeass'


def automate_chatbot(message):
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

    # Type the message
    pyautogui.typewrite(message)

    # Press "Enter" key to send the message
    pyautogui.press('enter')


def main():
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN #{channel}\r\n".encode('utf-8'))

    try:
        initial_prompt = True

        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                message = resp.split(':')[-1].strip()

                if initial_prompt:
                    # Ignore the initial prompt
                    initial_prompt = False
                else:
                    # Clear console before printing the new message
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if not message.startswith('End of /NAMES list'):
                        print(message)
                        automate_chatbot(message)

    except KeyboardInterrupt:
        sock.close()
        exit()


if __name__ == '__main__':
    main()
