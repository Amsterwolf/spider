import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
url="http://www.santostang.com"
headers={
    'user_agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"

}
r=requests.get(url,headers=headers)

html=etree.HTML(r.text)
title_list=html.xpath('/html/body/div//article/header/h1/a/text()')
print(title_list)



