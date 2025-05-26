import fetch
import autolive
import start
my_api= 'AIzaSyBOMzh5Uvp2RNhFdn1Z7Br2D2bVc6Nyvrs'

fbi="UCvLSQGgj08vC0ws_9f-Eung"

def main():
    print("Hello from stream-snip!")
    
    vid_id=autolive.check_live_stream(fbi)
    
    if vid_id:
        strt_time = start.get_start_time_ist(vid_id,my_api)
        print(strt_time)
        fetch.read(vid_id,strt_time)
        
    
if __name__ == "__main__":
    main()
