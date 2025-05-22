import requests
import re
import json
from datetime import datetime
import pytz

def get_start_time_ist(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return None

    # Search for the ytInitialPlayerResponse JSON
    match = re.search(r'ytInitialPlayerResponse\s*=\s*({.+?});', response.text)
    if not match:
        print("Could not find ytInitialPlayerResponse in the page.")
        return None

    # Parse the JSON data
    data = json.loads(match.group(1))

    try:
        start_time_str = data['microformat']['playerMicroformatRenderer']['liveBroadcastDetails']['startTimestamp']
        # Parse the UTC time
        utc_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S%z')
        # Convert to IST
        ist_timezone = pytz.timezone('Asia/Kolkata')
        ist_time = utc_time.astimezone(ist_timezone)
        return ist_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    except KeyError:
        print("Start timestamp not found in the data.")
        return None



