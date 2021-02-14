import requests
from bs4 import BeautifulSoup

url="https://www.w3school.com.cn/"
headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
r=requests.get(url,headers=headers)
print('r.encode:',r.encoding)#显示非utf-8
r.encoding='gbk'#解码格式
soup=BeautifulSoup(r.text,'lxml')
title=soup.find("div",id='d1').h2.text
print(title)