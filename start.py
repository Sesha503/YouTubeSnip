import requests
import re
import json
from datetime import datetime
import pytz

def get_start_time_ist(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.93 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return None

    match = re.search(r'ytInitialPlayerResponse\s*=\s*({.+?});', response.text)
    if not match:
        print("Could not find ytInitialPlayerResponse in the page.")
        return None

    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        print("Failed to parse ytInitialPlayerResponse JSON.")
        return None

    details = data.get('microformat', {}).get('playerMicroformatRenderer', {}).get('liveBroadcastDetails', {})
    start_time_str = details.get('startTimestamp')
    if not start_time_str:
        print("Start timestamp not found in the data.")
        return None

    utc_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S%z')
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = utc_time.astimezone(ist_timezone)
    return ist_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')




