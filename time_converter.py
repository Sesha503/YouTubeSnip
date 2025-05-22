from datetime import datetime
import pytz

def convert_unix_ms_to_ist(unix_ms):
    # Convert milliseconds to seconds
    unix_sec = unix_ms / 1000.0

    # Create a UTC datetime object
    utc_dt = datetime.utcfromtimestamp(unix_sec)

    # Define the IST timezone
    ist_tz = pytz.timezone('Asia/Kolkata')

    # Localize the UTC datetime to IST
    ist_dt = pytz.utc.localize(utc_dt).astimezone(ist_tz)

    # Format the datetime
    formatted_time = ist_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return formatted_time