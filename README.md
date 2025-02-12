# Twitter-Agent

Twitter-Agent is a Python script that generates tweets using an LLM model and posts them to Twitter via the Twitter API.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.8 or higher
- `requests` library
- `requests_oauthlib` library
- `python-dotenv` library

You can install the required dependencies using:

```bash
pip install requests requests_oauthlib python-dotenv
```

## Setup

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com/VyxaFoundation/Twitter-Agent.git
   cd Twitter-Agent
   ```

2. **Create a `.env` file** in the project root and add the following environment variables:

   ```
   # Twitter API Credentials
   TWITTER_CONSUMER_KEY=your_consumer_key
   TWITTER_CONSUMER_SECRET=your_consumer_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

   # LLM API Configuration
   OLLAMA_API_URL=http://localhost:11434/api/generate
   LLM_MODEL=VyxaFoundation/Vyxa
   ```

   - Replace `your_consumer_key`, `your_consumer_secret`, `your_access_token`, and `your_access_token_secret` with your actual Twitter API credentials.
   - Ensure `OLLAMA_API_URL` points to your running LLM API endpoint.

## Running the Script

To run the script, execute:

```bash
python twitterAgent.py
```

## Expected Behavior

- The script will request a tweet from the LLM model.
- If a valid response is received, it will attempt to post the tweet to Twitter.
- A success or failure message will be displayed in the terminal.

## Troubleshooting

- Ensure all environment variables are set correctly.
- Check if the LLM API is running at the specified `OLLAMA_API_URL`.
- Verify that your Twitter API credentials are correct and have tweet posting permissions.

## License

This project is open-source under the Vyxa Foundation.



## Stay Connected

💻 **Website:** [Vyxa.org](https://www.vyxa.org/)  
📂 **GitHub:** [Vyxa GitHub](https://github.com/VyxaFoundation)  
𝕏 **Twitter/X:** [@VyxaFoundation](https://x.com/vyxaFoundation)
