import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BROADCASTER_NAME = os.getenv("BROADCASTER_NAME")

# Get OAuth token
auth_url = 'https://id.twitch.tv/oauth2/token'
auth_params = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'client_credentials'
}

auth_response = requests.post(auth_url, data=auth_params)
auth_response.raise_for_status()
access_token = auth_response.json()['access_token']

# Get User ID
headers = {
    'Client-ID': CLIENT_ID,
    'Authorization': f'Bearer {access_token}'
}

user_url = f'https://api.twitch.tv/helix/users?login={BROADCASTER_NAME}'
response = requests.get(user_url, headers=headers)
response.raise_for_status()
user_id = response.json()['data'][0]['id']

# Get all VODs with pagination
vods_url = f'https://api.twitch.tv/helix/videos?user_id={user_id}&first=100'
vods_data = []

while vods_url:
    response = requests.get(vods_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    vods_data.extend(data['data'])

    # Get the pagination cursor
    cursor = data.get('pagination', {}).get('cursor')
    if cursor:
        vods_url = f'https://api.twitch.tv/helix/videos?user_id={user_id}&first=100&after={cursor}'
    else:
        vods_url = None

# Convert to DataFrame
df = pd.DataFrame(vods_data)
df = df[['id', 'title', 'created_at', 'type', 'duration', 'url']]
df.columns = ['VOD_ID', 'Title', 'Created_At', 'Type', 'Duration', 'URL']

# Save to Excel
output_filename = "twitch_vods.xlsx"
df.to_excel(output_filename, index=False)

print(f"Total videos scraped: {len(df)}")
print(f'All VOD data saved to {output_filename}!')