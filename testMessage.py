import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv  # ✅ dotenv added

# Load environment variables from .env file
load_dotenv() 

# Load Twitter API credentials from environment variables (More secure)
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Twitter API URL
TWITTER_API_URL = "https://api.twitter.com/2/tweets"

def post_tweet(message: str):
    """Posts a tweet using the Twitter API."""
    if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        raise ValueError("❌ Missing Twitter API credentials. Set them as environment variables.")

    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    payload = {"text": message}

    try:
        response = requests.post(TWITTER_API_URL, json=payload, auth=auth)
        response_data = response.json()

        if response.status_code == 201:
            tweet_id = response_data.get("data", {}).get("id")
            print(f"✅ Tweet successfully posted! ID: {tweet_id}")
            return tweet_id
        else:
            print(f"❌ Failed to post tweet: {response_data}")
            return None
    except requests.RequestException as e:
        print(f"⚠️ Error sending request: {e}")
        return None

if __name__ == "__main__":
    tweet_text = "Test tweet from the Vyxa Foundation Twitter-Agent repository! Stay tuned for more updates."
    post_tweet(tweet_text)
