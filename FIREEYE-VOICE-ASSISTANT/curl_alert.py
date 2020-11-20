import requests
import time
from datetime import datetime

def curl(url):
    while(True):
        r = requests.get(url)  #change the url of your choice to check whether it's live
        now = datetime.now()
        log = open("./request_log.txt","a")
        log.write(str(now) + " - " + str(r) + "\n")
        log.close()
        if "<Response [200]>" in str(r):
            print("Website is Up!  -   [ " + str(now) + " ]")
            exit()
        else:
            time.sleep(2)
            continue
curl("http://www.google.com")

