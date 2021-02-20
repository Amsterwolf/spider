from redis import Redis
import requests
from bs4 import BeautifulSoup
import json
import time

headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

}

def push_redis_list():
    '''连接redis服务器，上传下载列表'''
    red=Redis(host='159.75.140.116',port=3145,password='basketball')
    print(red.keys('*'))

    with open('sites.json','r') as f:
        url_list=json.load(f)
    for url in url_list:
        try:
            r=requests.get(url,headers=headers,timeout=10)
            soup=BeautifulSoup(r.text,'lxml')
            img_tag_list=soup.find_all("img")
            for img_tag in img_tag_list:
                img_url=img_tag['src']
                if img_url!='':
                    print("待下载的图片的url:",img_url)
                    red.lpush('img_url',img_url)
            print("队列url数：",red.llen('img_url'))
        except Exception as e:
            print("error:",e)




def get_image():
    '''连接redis服务器，获取图片下载列表并下载'''
    red=Redis(host='159.75.140.116',port=3145,password='basketball')
    while red.llen('img_url'):
        try:
            url=red.lpop('img_url').decode("ascii") 
            if url[:2]=='//':
                url='https:'+url
            print('img url:',url)
            r=requests.get(url,headers=headers,timeout=10)
            file_name=str(int(time.time()))
            with open(file_name+url[-4:],'wb') as f:
                f.write(r.content)
            print("已下载图片：",url)
        except Exception as e:
            print(e)
            time.sleep(10)

if __name__=='__main__':
    this_machine='master'
    print("开始分布式爬虫")
    if this_machine=='master':
        push_redis_list()
    else:
        get_image()

