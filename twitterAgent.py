import os
import re
import json
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv  

# Load environment variables
load_dotenv()

# Required environment variables
REQUIRED_ENV_VARS = [
    "TWITTER_CONSUMER_KEY", "TWITTER_CONSUMER_SECRET", 
    "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN_SECRET",
    "OLLAMA_API_URL", "LLM_MODEL"
]

def validate_env_vars():
    """Ensures all required environment variables are set."""
    missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"❌ Missing environment variables: {', '.join(missing_vars)}")

validate_env_vars()

# API credentials
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")
LLM_MODEL = os.getenv("LLM_MODEL")

# ✅ FIXED: Define Twitter API URL
TWITTER_API_URL = "https://api.twitter.com/2/tweets"

# LLM Prompt
PROMPT = "Tell me something about Solana in 160 characters."

def clean_response(response_text):
    """
    Removes unwanted <think>...</think> tags from the model's response.
    """
    return re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()

def make_request(url, method="GET", json_data=None, auth=None):
    """
    Generalized function to handle API requests.
    """
    try:
        response = requests.request(method, url, json=json_data, auth=auth)
        response.raise_for_status()  # Raise error for HTTP issues
        return response.json()
    except requests.RequestException as e:
        print(f"⚠️ API Error: {e}")
        return None

def ask_LLM():
    """
    Sends a request to the LLM and returns the cleaned response.
    """
    response = make_request(OLLAMA_API_URL, method="POST", json_data={
        "model": LLM_MODEL,
        "prompt": PROMPT,
        "stream": False,
        "options": {"temperature": 0}
    })

    if response and "response" in response:
        return clean_response(response["response"])
    
    print("❌ Failed to get a response from the LLM.")
    return None

def post_tweet(message):
    """
    Posts a tweet using the Twitter API.
    """
    if not message:
        print("⚠️ Cannot post an empty tweet.")
        return None

    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = make_request(TWITTER_API_URL, method="POST", json_data={"text": message}, auth=auth)

    if response and response.get("data"):
        tweet_id = response["data"]["id"]
        print(f"✅ Tweet successfully posted! ID: {tweet_id}")
        return tweet_id
    
    print("❌ Failed to post the tweet.")
    return None

if __name__ == "__main__":
    tweet_content = ask_LLM()
    post_tweet(tweet_content)
