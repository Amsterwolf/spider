import requests
from bs4 import BeautifulSoup
import time
#测试单线程爬虫爬取100个网页的速度

#先从alexa.cn网站获取1000个访问量最大的中文网站
def get_list(filepath):
    f=open(filepath,'a+',encoding='utf-8')
    for page in range(1,51):
        
        url='http://www.alexa.cn/siterank/'+str(page)
        headers={
            "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

        }
        r=requests.get(url,headers=headers)
        soup=BeautifulSoup(r.content.decode('utf-8'),'lxml')
        div_tag_list=soup.find_all('div',class_="domain")
        link_list=[div.a['href'].split('/')[-1] for div in div_tag_list]
        for i in link_list:
            f_link='http://www.'+i
            f.write(f_link+'\n')

    f.close()    
        

filepath="site_rank.txt"
#get_list(filepath)
link_list=[]
with open(filepath,'r') as f:
    file_list=f.readlines()
    for row in file_list:
        link=row.replace('\n','')
        link_list.append(link)

st=time.time()
for link in link_list:
    try:
        r=requests.get(link,headers={
            "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        },timeout=3
        )
        print(r.status_code,link)
    except Exception as e:
        print("Error:",e)
ed=time.time()
print("串行的时间:",ed-st)

