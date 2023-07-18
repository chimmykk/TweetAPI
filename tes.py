import os
import socket

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'rilsos'
token = 'oauth:wb7ph6zjttttvdtk9x3uz27vy8umdi'
channel = 'dylansafeass'

message_count = 1  # Counter for the message files

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

                        # Save message to a text file
                        save_message_to_file(message)

                        # Retrieve the last message file
                        file_path = os.path.join('tobereadnow', f"{message_count}.txt")
                        if os.path.exists(file_path):
                            with open(file_path, 'r', encoding='utf-8') as file:
                                input_message = file.read()

                            # Pass the input message to the chatbot function
                            automate_chatbot(input_message)

    except KeyboardInterrupt:
        sock.close()
        exit()

def save_message_to_file(message):
    global message_count
    folder_name = 'tobereadnow'
    file_name = f"{message_count}.txt"
    file_path = os.path.join(folder_name, file_name)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(message)

    message_count += 1

def automate_chatbot(input_message):
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

    # Type the input message obtained from the file
    pyautogui.typewrite(input_message)

    # Press "Enter" key to send the message
    pyautogui.press('enter')

if __name__ == '__main__':
    main()
