import fetch
import autolive
import start
#my api= AIzaSyBOMzh5Uvp2RNhFdn1Z7Br2D2bVc6Nyvrs

fbi="UCvLSQGgj08vC0ws_9f-Eung"

def main():
    print("Hello from stream-snip!")
    
    vid_id=autolive.check_live_stream(fbi)
    
    if vid_id:
        strt_time = '2025-05-23 16:13:42 IST+0530'
        print(strt_time)
        fetch.read(vid_id,strt_time)
        
    
if __name__ == "__main__":
    main()
