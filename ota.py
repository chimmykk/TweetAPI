import os
import socket
import subprocess
import time
import pyautogui
import threading
from queue import Queue

# Global variables
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'rilsos'
token = 'oauth:wb7ph6zjttttvdtk9x3uz27vy8umdi'
channel = 'dylansafeass'

output_folder = "tobereadnow"
message_queue = Queue()

# Variables for the application process
app_process = None
app_opened = False
application_path = r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe'


def main():
    # Clear console before connecting to the IRC server
    os.system('cls' if os.name == 'nt' else 'clear')

    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN #{channel}\r\n".encode('utf-8'))

    message_processor_thread = threading.Thread(target=process_message_queue)
    message_processor_thread.start()

    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                message = resp.split(':')[-1].strip()

                # Clear console before printing the new message
                os.system('cls' if os.name == 'nt' else 'clear')

                if not message.startswith('End of /NAMES list'):
                    print(message)

                    # Add the message to the queue
                    message_queue.put(message)

    except KeyboardInterrupt:
        sock.close()
        message_queue.join()
        exit()


def process_message_queue():
    while True:
        message = message_queue.get()
        save_message_to_file(message)
        message_queue.task_done()


def save_message_to_file(message):
    filename = os.path.join(output_folder, 'theprompt.txt')
    with open(filename, 'a') as file:
        file.write(message + '\n')


def automate_chatbot_with_message(message):
    global app_process, app_opened

    if not app_opened:
        # Open the application if it is not already open
        app_process = subprocess.Popen([application_path])
        app_opened = True

        # Wait for the application to open (adjust the sleep time as needed)
        time.sleep(5)

    # Perform the automation steps using the opened application
    if app_opened:
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

        # Type the message from the console
        pyautogui.typewrite(message)

        # Press "Enter" key to send the message
        pyautogui.press('enter')


if __name__ == '__main__':
    main()
