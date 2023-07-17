import subprocess
import time
import pyautogui
import requests
import os
import tweepy
live_687526658_hN26OxWG5G13flbJk95hqO4ZZCmgRZ
# Set bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAACzGoQEAAAAAPBUyxZyXrtNzab8B3guBR9e994k%3DDieBbwNezSIZ26haV9I17LcWMpOf2z7nPkC9gYKFJEwL0AnTF3"

# Set endpoint URL
endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

# Replace with your actual consumer key and secret
CONSUMER_KEY = "Vkm90x8yGmUtAJSNCcUSlh7TX"
CONSUMER_SEC = "hRusPRyjS72NZ2uvKzRpmTDkeJL6FKNsQGvz9t7o6oaj9v5gz1"

# Replace with your actual access token and secret
AUTH_ACC = "1576014870084030465-eNPRHtueYUoaxKlYJKWVgtnxgzk1Jq"
AUTH_SEC = "xD9IXgJjthdxLzqn9b76i1k0GtKYT0TPeyyMdEIPhHOSl"

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
            bandicam_process = subprocess.Popen(r'"C:\Program Files\Bandicam\bdcam.exe"')

            time.sleep(2)  # Adjust the sleep time based on the required wait for Bandicam to start

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

            # Authenticate using API v1.1
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
            auth.set_access_token(AUTH_ACC, AUTH_SEC)
            api = tweepy.API(auth, wait_on_rate_limit=True)

            # Authenticate using API v2.0
            client = tweepy.Client(bearer_token, CONSUMER_KEY, CONSUMER_SEC, AUTH_ACC, AUTH_SEC, wait_on_rate_limit=True)

            try:
                api.verify_credentials()
                print("V1.1 Authentication OK")
            except Exception as e:
                print(f"Error during authentication: {e}")

            # Set the file path and status text
            if media_files:
                file_path = media_files[0]  # Assuming the first media file found is the one to be posted
                status_text = "Message with media"

                # Media upload through API v1.1
                media_info = api.media_upload(filename=file_path)

                # Tweet posting through API v2.0
                tweet = client.create_tweet(text=status_text, media_ids=[media_info.media_id], in_reply_to_tweet_id=tweet_id)
                print("Reply posted successfully.")

except Exception as e:
    print(e)
