import requests
from bs4 import BeautifulSoup
import json

'''从网站爬取user-agent,以列表形式存入fake_ua.json'''

url="http://www.useragentstring.com/pages/useragentstring.php?name=Chrome"
headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'lxml')
div_tag=soup.find("div",id='liste')
ul_tag_list=div_tag.find_all('ul')
fake_useragent_list=[]
for ul in ul_tag_list:
    fake_useragent_list.append(ul.li.a.text)

with open('fake_ua.json','w') as f:
    json.dump(fake_useragent_list,f)
