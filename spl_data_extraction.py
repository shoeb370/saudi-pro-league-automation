import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go
from post_tweet_v2 import post_tweet

# URL of the league table
url = 'https://www.spl.com.sa/en/table'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table
    table = soup.find('table')
    
    # Extract headers
    headers = [header.text.split()[0].strip() for header in table.find_all('th')]
    
    # Clean headers
    headers = [header.replace(' ', '') for header in headers]
    
    # Extract rows
    rows = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        cols[-1] = '-'.join(cols[-1].split())
        rows.append(cols)
    
    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)
    
    # Print the DataFrame
    print(df)
    # Create the table
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df[col] for col in df.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    
    # fig.update_layout(height=1200)  # Adjust the height as needed
    fig.update_layout(
    height=450,  # Adjust height
    width=1000,  # Adjust width
    margin=dict(l=10, r=10, t=10, b=10)  # Adjust margins to reduce white space
)
    # Save the table as an image
    fig.write_image("df_image.png", engine="kaleido")
    twitter_post = """
        🏆 Saudi Pro League Points Table 🏆
        #SaudiProLeague #Football #Soccer #SaudiArabia #SPL #saudileague
        """

    print(twitter_post)
    post_tweet(twitter_post, 'df_image.png')

    
    # Show the table
    fig.show()
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
