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

message_count = 3  # Start reading from 3.txt

chatbot_process = None

def main():
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

                print(message)

                # Save message to a text file
                save_message_to_file(message)

                # Automate chatbot using the message from the file
                automate_chatbot_with_message_from_file()

    except KeyboardInterrupt:
        sock.close()
        exit()

def save_message_to_file(message):
    global message_count
    folder_name = 'toreadnow'
    file_name = f"{message_count}.txt"
    file_path = os.path.join(folder_name, file_name)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(message)

    message_count += 1

def automate_chatbot_with_message(message):
    global chatbot_process

    time.sleep(2)

    # Type the message from the file
    pyautogui.typewrite(message)

    # Press "Enter" key to send the message
    pyautogui.press('enter')

def automate_chatbot_with_message_from_file():
    global message_count, chatbot_process

    folder_name = 'toreadnow'

    while True:
        file_name = f"{message_count}.txt"
        file_path = os.path.join(folder_name, file_name)

        if not os.path.exists(file_path):
            break

        with open(file_path, 'r', encoding='utf-8') as file:
            message = file.read().strip()

        if chatbot_process is None:
            chatbot_process = subprocess.Popen(r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe', shell=True)
            time.sleep(2)
            # Press "Tab" key three times to navigate to the Doge option
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            # Press "Enter" key to select the Doge option
            pyautogui.press('enter')
            
        automate_chatbot_with_message(message)
        message_count += 1

if __name__ == '__main__':
    main()
