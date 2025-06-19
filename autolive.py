from googleapiclient.discovery import build
import os

my_api= os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def check_live_stream(chnl_id):
    request = youtube.search().list(
        part="snippet",
        channelId=chnl_id,
        eventType="live",
        type="video"
    )
    response = request.execute()
    return response['items'][0]['id']['videoId'] if response['items'] else None
