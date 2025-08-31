import fetch
import autolive
import start
import os
my_api= os.getenv('API_KEY')

def main():
    print("Hello from stream-snip!")
    
    vid_id=autolive.check_live_stream(os.getenv('CHANNEL_ID'))
    
    if vid_id:
        strt_time = start.get_start_time_ist_api(vid_id,my_api)
        print(strt_time)
        fetch.read(vid_id,strt_time)
        
    
if __name__ == "__main__":
    main()
