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
