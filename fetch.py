import pytchat
import time
import discord
from datetime import datetime
import time_converter as tc
import deltatime
import os
dwh = os.getenv('DISCORD_WEBHOOK')

def read(video_id,str_time):
    print(f" Listening for !clip in live chat of https://www.youtube.com/watch?v={video_id}")
    chat = pytchat.create(video_id=video_id)
    count = 1

    while chat.is_alive():
        chatdata = chat.get()
        for c in chatdata.sync_items():
            comment = c.message.split(" ")
            #if "!clip" == comment[0] and (c.author.isChatOwner or c.author.isChatModerator):
            if "!clip" == comment[0].lower():
                if len(comment) > 1:
                    clip_title = " ".join(comment[1:])
                else:
                    clip_title = "Untitled" + str(count)
                    count += 1
               
                tmstp = tc.convert_unix_ms_to_ist(c.timestamp)
                timlist = deltatime.delta(tmstp,str_time)
                timsec= int(timlist[0])

                content=f"  Clip Request by {c.author.name} \n  Title: {clip_title} \n  Link : https://www.youtube.com/watch?v={video_id}&t={timsec}s \n  Timestamp: {timlist[1]} \n  Delayed by 59 Seconds "

                discord.send_to_discord(dwh,content)
        time.sleep(1)





