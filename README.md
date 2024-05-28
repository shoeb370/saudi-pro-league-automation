# Saudi Pro League Automation
![Saudi Pro League Logo](https://github.com/shoeb370/saudi-pro-league-automation/assets/36133933/f2036546-9a68-4b2b-85ba-990394a338b2)

This project automates the extraction, processing, visualization, and tweeting of the Saudi Pro League points table. It uses web scraping to gather data from the official Saudi Pro League website, processes the data with pandas, visualizes it using Plotly, and posts the table as an image to Twitter.

## Features

- Web scraping of the Saudi Pro League points table
- Data processing and cleaning with pandas
- Visualization of the points table using Plotly
- Automated posting of the table image to Twitter

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `plotly` library
- `kaleido` library for saving Plotly images
- A Twitter posting function (placeholder provided)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/saudi-pro-league-automation.git
   cd saudi-pro-league-automation
   
3. Install the required Python packages:
   ```bash
    pip install requests beautifulsoup4 pandas plotly kaleido

  

## Twitter API Setup

1. **Create a Twitter Developer Account**: Sign up for a Twitter Developer account at [Twitter Developer](https://developer.twitter.com/).
  
2. **Create a New App**: Once logged in to the Twitter Developer Portal, create a new app and note down the following credentials:
   - API key
   - API secret key
   - Access token
   - Access token secret
   
3. **Configure config_tweet.ini**: Create a `config_tweet.ini` file in the project directory with the following format:
   ```ini
   [Twitter]
   api_key = YOUR_API_KEY
   api_secret = YOUR_API_SECRET
   access_token = YOUR_ACCESS_TOKEN
   access_secret_token = YOUR_ACCESS_SECRET_TOKEN
   bearer_token = YOUR_BEARER_TOKEN
4. Update the auth_cred() function in post_tweet_v2.py to read these credentials from config_tweet.ini

## Authentication and Tweet Posting

The `auth_cred()` function reads the Twitter API credentials from `config_tweet.ini` and authenticates the API client using `tweepy.Client` and `tweepy.OAuth1UserHandler`.

The `post_tweet(tweet, file_name)` function in `post_tweet_v2.py` posts a tweet with the provided tweet content and an optional image (`file_name`).

## Usage

1. Ensure `config_tweet.ini` is correctly configured with your Twitter API credentials.
2. Run the `spl_data_extraction.py` script to fetch the points table from Saudi Pro League website.


## Contributors

- [Shoeb Ahmed](https://github.com/shoeb370)
## Sponsorship
Thank you for considering supporting this project! Your sponsorship helps in maintaining and improving this project.

Supported Funding Platforms:
- PayPal: [Donate Now](https://www.paypal.me/shoeb370)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

