import os
import requests
import json
import subprocess
import time
import pyautogui

# Global variables
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'rilsos'
token = 'oauth:sp86qcmj6kvbqfz6pqmt8nbsvk5sj4'
channel = 'thedogeai'

# Variables for the application process
app_process = None
app_opened = False
application_path = r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe'

def fetch_news(category):
    """Fetches news from the News API based on the provided category."""
    url = f"https://newsapi.org/v2/everything?q={category}&language=en&sortBy=publishedAt&apiKey=0d82bbd91c974f81ae2df4b190404fbd"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["articles"]
    else:
        return None

def main():
    global app_opened
    app_opened = False

    categories = ["crypto", "sports", "weather", "worldnews"]
    for category in categories:
        news = fetch_news(category)
        if news is not None:
            folder_name = category
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            file_name = f"{category}_news.txt"
            file_path = os.path.join(folder_name, file_name)

            with open(file_path, "w", encoding="utf-8") as file:
                for article in news:
                    title = article["title"]
                    description = article["description"]
                    file.write(title + "\n")
                    file.write(description + "\n")
                    file.write("@\n")  # Add "@" symbol at the end of each article

            print(f"{category.capitalize()} news saved to {file_path}.")
        else:
            print(f"Failed to fetch {category} news.")

    # Read messages from the crypto folder and process them
    folders = ["crypto", "sports", "weather", "worldnews"]
    for folder in folders:
        process_folder(folder)

def process_folder(folder):
    folder_path = os.path.join(os.getcwd(), folder)
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:  # Specify encoding as utf-8
                    message = file.read()
                    sentences = extract_sentences_from_message(message)

                    # Perform the automation steps using the opened application
                    if not app_opened:
                        # Open the application if it is not already open
                        global app_process
                        app_process = subprocess.Popen([application_path])
                        app_opened = True

                        # Wait for the application to open (adjust the sleep time as needed)
                        time.sleep(5)

                    if app_opened:
                        for sentence in sentences:
                            # Trigger three tabs
                            pyautogui.rightClick()
                            pyautogui.press('tab')
                            pyautogui.press('tab')
                            pyautogui.press('tab')

                            # Extracted sentence from the message is passed to typewrite
                            pyautogui.typewrite(sentence)

                            # Press "Enter" key to send the message
                            pyautogui.press('enter')

def extract_sentences_from_message(message):
    # Split the message into sentences using "@" as the delimiter
    sentences = message.split("@")
    # Filter out any empty sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

if __name__ == '__main__':
    main()
