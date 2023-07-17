import subprocess
import time
import pyautogui
import requests
import os
import tweepy

# Set bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAACzGoQEAAAAAPBUyxZyXrtNzab8B3guBR9e994k%3DDieBbwNezSIZ26haV9I17LcWMpOf2z7nPkC9gYKFJEwL0AnTF3"

# Set endpoint URL
endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

# Set Twitter API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

def get_request():
    # Edit query parameters below
    # Specify a search query, and any additional fields that are required
    # By default, only the Tweet ID and text fields are returned
    params = {
        'query': '@doge_gm -is:retweet',
        'tweet.fields': 'author_id'
    }

    headers = {
        "User-Agent": "v2RecentSearchPython",
        "Authorization": f"Bearer {bearer_token}"
    }

    response = requests.get(endpoint_url, params=params, headers=headers)
    response_json = response.json()

    if response.status_code == 200:
        return response_json
    else:
        raise Exception('Unsuccessful request')

def upload_tweet(media_files, tweet_id):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Upload or send the tweet
    if len(media_files) > 0:
        media_ids = []
        for media_file in media_files:
            media = api.media_upload(media_file)
            media_ids.append(media.media_id)

        api.update_status(status=f"Tweet with Media ID: {tweet_id}", media_ids=media_ids)
    else:
        api.update_status(status=f"Tweet without Media ID: {tweet_id}")

try:
    # Make request
    response = get_request()

    # Display the first recent mention with text and tweet ID
    if 'data' in response and len(response['data']) > 0:
        tweet = response['data'][0]
        if 'text' in tweet and 'id' in tweet:
            tweet_text = tweet['text']
            tweet_id = tweet['id']
            print("Tweet ID:", tweet_id)
            print("Tweet Text:", tweet_text)

            # Open the chatbot application
            subprocess.Popen(r'C:\Users\paperspace\Downloads\AllCharactersAI_v0.18\AllCharactersAI_v0.18\Windows\Chatbot_Characters.exe')

            time.sleep(2)

            # Run Bandicam application
            bandicam_process = subprocess.Popen(r'C:\Program Files\Bandicam\bdcam.exe')

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

            # Type the generated tweet text as the message
            pyautogui.typewrite(tweet_text)

            # Press "Enter" key to send the message
            pyautogui.press('enter')

            # Add a 2-second delay
            time.sleep(2)

            # Press F12 button after opening Bandicam
            pyautogui.press('f12')

            # Wait for 1 minute
            time.sleep(60)

            # Press F12 button again to stop recording
            pyautogui.press('f12')

            # Wait for Bandicam process to terminate
            bandicam_process.wait()

            # Extract the tweet ID and find media files
            print("Extracted Tweet ID:", tweet_id)

            media_path = r"C:\Users\paperspace\Documents\Bandicam"
            media_files = []

            if os.path.exists(media_path) and os.path.isdir(media_path):
                for file in os.listdir(media_path):
                    file_path = os.path.join(media_path, file)
                    if os.path.isfile(file_path):
                        media_files.append(file_path)

            print("Media Files Found:")
            for media_file in media_files:
                print(media_file)

            # Upload or send tweet with media
            upload_tweet(media_files, tweet_id)

except Exception as e:
    print(e)
