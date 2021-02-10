import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

#连接至客户端
client=MongoClient('localhost',27017)
#连接（新建）数据库
db=client.atestdb
#连接（新建）集合（表）
collection=db.blog


url="http://www.santostang.com/"
headers={
    "usr_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

}
r=requests.get(url,headers=headers)

soup=BeautifulSoup(r.text,'lxml')
h1_list=soup.find_all("h1",class_="post-title")
a_list=[i.a for i in h1_list]
for a in a_list:
    url=a['href']
    #print(url)
    content=a.text
    #print(content)
    post={
        'url':url,
        'title':content,
        'date':datetime.datetime.utcnow(),

    }
    collection.insert_one(post)


  
