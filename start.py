import requests
from datetime import datetime
import pytz

def get_start_time_ist_api(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={video_id}&key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"API error: {response.status_code}")
        return None

    data = response.json()
    try:
        start_time_str = data['items'][0]['liveStreamingDetails']['actualStartTime']
        utc_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.UTC)
        ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
        return ist_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    except (IndexError, KeyError):
        print("Live start time not found.")
        return None
