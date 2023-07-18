import os
import socket
import subprocess
import time
import pyautogui

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'rilsos'
token = 'oauth:wb7ph6zjttttvdtk9x3uz27vy8umdi'
channel = 'dylansafeass'

output_folder = "tobereadnow"
file_counter = 1

chatbot_process = None  # Global variable to store the chatbot subprocess
last_activity_time = time.time()  # Track the last activity time

def main():
    # Clear console before connecting to the IRC server
    os.system('cls' if os.name == 'nt' else 'clear')

    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN #{channel}\r\n".encode('utf-8'))

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

                    # Store the message to a text file
                    store_message_to_file(message)

                    # Automate chatbot using the message from the console
                    automate_chatbot_with_message(message)

                    # Check if 2 minutes have elapsed since the last activity
                    current_time = time.time()
                    if current_time - last_activity_time >= 120:
                        close_chatbot_process()
                        last_activity_time = current_time  # Update the last activity time

    except KeyboardInterrupt:
        close_chatbot_process()
        sock.close()
        exit()


def store_message_to_file(message):
    global file_counter
    filename = f"{output_folder}/{file_counter}.txt"
    with open(filename, 'w') as file:
        file.write(message)
    file_counter += 1


def automate_chatbot_with_message(message):
    global chatbot_process

    if chatbot_process is None or chatbot_process.poll() is not None:
        # Chatbot process is not running or has exited, so start a new one
        chatbot_process = subprocess.Popen(r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe')
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

    # Type the message from the console
    pyautogui.typewrite(message)

    # Press "Enter" key to send the message
    pyautogui.press('enter')


def close_chatbot_process():
    global chatbot_process

    if chatbot_process is not None and chatbot_process.poll() is None:
        # Chatbot process is running, so terminate it
        chatbot_process.terminate()
        chatbot_process.wait()  # Wait for the process to exit


if __name__ == '__main__':
    main()
