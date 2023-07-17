import subprocess
import time
import pyautogui
import requests

# Set bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAACzGoQEAAAAAPBUyxZyXrtNzab8B3guBR9e994k%3DDieBbwNezSIZ26haV9I17LcWMpOf2z7nPkC9gYKFJEwL0AnTF3"

# Set endpoint URL
endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

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

except Exception as e:
    print(e)
