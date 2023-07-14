import subprocess
import time
import pyautogui
import os
import dropbox
from dropbox.exceptions import AuthError

# Dropbox access token
DROPBOX_ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'

# Folder path to check for videos
VIDEO_FOLDER_PATH = r'C:\Users\paperspace\Videos\Chatbot_characters'

def upload_video_to_dropbox(video_path):
    # Initialize Dropbox client
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

    try:
        # Upload the video file to Dropbox
        with open(video_path, 'rb') as file:
            dbx.files_upload(file.read(), '/' + os.path.basename(video_path))
        print("Video uploaded to Dropbox successfully.")
    except AuthError as e:
        print("Error authenticating with Dropbox.")
    except dropbox.exceptions.ApiError as e:
        print("Error uploading video to Dropbox:", e)

def automate_chatbot_and_upload():
    # Open the chatbot application
    subprocess.Popen(r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe')

    time.sleep(2)

    # Rest of the code to automate the chatbot interactions...

    # Add a 2-second delay
    time.sleep(2)

    # Enable screen recording
    pyautogui.hotkey('alt', 'f9')

    # Wait for 1 minute
    time.sleep(60)

    # Close the application
    pyautogui.hotkey('alt', 'f4')

    # Check for video files in the folder
    video_files = [file for file in os.listdir(VIDEO_FOLDER_PATH) if file.endswith('.mp4')]

    if video_files:
        print("Found video files:", video_files)
        for video_file in video_files:
            video_path = os.path.join(VIDEO_FOLDER_PATH, video_file)
            upload_video_to_dropbox(video_path)
    else:
        print("No video files found in the folder.")

automate_chatbot_and_upload()
