import requests
import time
import random
from change_ip import Asdl
headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

}

def crawl(url,try_times=3):
    '''返回网页文本，爬取失败时换ip'''
    try:
        r=requests.get(url,headers=headers)
        html=r.text
        time.sleep(random.randrange(2.0,5.0))
        return html
    except Exception as e:
        print(e)
        if try_times>0:
            a=Asdl()
            a.reconnect()
            return crawl(url,try_times-1)
        else 
            return None
    