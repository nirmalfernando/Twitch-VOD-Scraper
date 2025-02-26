# Twitch VOD Scraper

A Python project to fetch all VODs (Videos on Demand) from a Twitch broadcaster using the Twitch API and save them in an Excel file. This project also includes a script to filter videos under a specific duration and save them in a separate Excel file.

⚠️ **Important Note:**  
The number of videos retrieved may sometimes be lower than the actual number of VODs available on the broadcaster's channel. Despite handling pagination correctly and making multiple attempts, the results remain consistent — leading to the guess that this could be due to some unexpected behavior from the Twitch API. This isn’t a confirmed issue, but if you experience this, double-check your API permissions and try again later.

---

## Features
- Fetch all available VODs from a specified Twitch broadcaster.
- Properly handles API pagination to avoid missing large batches of videos.
- Saves the video data in an Excel format (`.xlsx`).
- Includes a script to filter and save videos under **11 hours, 59 minutes, and 58 seconds** duration.
- Uses environment variables for secure API credentials management.

---

## Prerequisites
- Python 3.8+
- A **Twitch Developer Account** with a **registered app** to obtain `CLIENT_ID` and `CLIENT_SECRET`.  
  You can create an app and get these credentials at the [Twitch Developer Console](https://dev.twitch.tv/console/apps).

---

## Setup

1. **Clone the repository:**
```bash
git clone https://github.com/nirmalfernando/Twitch-VOD-Scraper.git
cd Twitch-VOD-Scraper
```

2. **(Optional) Create a virtual environment:**
```bash
# For Linux/Mac
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create a .env file in the project root and add your Twitch API credentials:**
```bash
CLIENT_ID=your_twitch_client_id
CLIENT_SECRET=your_twitch_client_secret
BROADCASTER_NAME=twitch_username     # The Twitch username whose VODs you want to fetch
```

5. **Run the VOD scraper script to get all VODs:**
```bash
python3 twitch_vod_scraper.py
```

This will:
- Authenticate with the Twitch API using your CLIENT_ID and CLIENT_SECRET.
- Retrieve all available VODs for the specified BROADCASTER_NAME.
- Save the video data into an Excel file called twitch_vods.xlsx.

6. **(Optional) Filter videos under 11h59m58s and save them to a new file:**
```bash
python3 filter_vods.py
```

This will:
- Load the twitch_vods.xlsx file.
- Filter videos with a duration less than 11h59m58s (43198 seconds).
- Save the filtered videos into filtered_twitch_vods.xlsx.

## Project Structure
```bash
Twitch-VOD-Scraper/
│
├── .env                        # Environment variables (API credentials)
├── requirements.txt            # Python dependencies
├── twitch_vod_scraper.py       # Main script to fetch VODs and save to Excel
├── filter_vods.py              # Script to filter and save videos under 11h59m58s
├── README.md                   # Project description and setup instructions
└── .gitignore                  # Ignore unnecessary files (like .env and Excel files)
```

