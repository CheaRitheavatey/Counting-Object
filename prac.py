# create automation social media posting on tiktok

import requests
import schedule
import time

def post_on_tiktok():
    url = "https://tiktok.com/@pandey_sudhanshu"
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully posted on tiktok")
    else:
        print("Failed to post on tiktok")
schedule.every(10).minutes.do(post_on_tiktok)

while True:
    schedule.run_pending()
    time.sleep(1)