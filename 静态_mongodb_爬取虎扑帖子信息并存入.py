import requests
from bs4 import BeautifulSoup

import datetime
from mongoapi import MongoAPI
import time
def modify_time(time):
    if ':' in time:#such as 20:30
        time=str(datetime.date.today())+' '+time
        date_time=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M')
    else:
        if time.find('-')!=4:#such as 11-27
            time='2021-'+time
        else:#such as 2020-11-27
            pass
        date_time=datetime.datetime.strptime(time,'%Y-%m-%d').date()
    return date_time

#连接mongodb，新建‘hupu’db,新建‘post’collection
connection=MongoAPI('hupu','post')

#爬取前10页帖子信息
for i in range(1,11):
    url="http://bbs.hupu.com/bxj-"+str(i)
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

    }
    r=requests.get(url,headers=headers)
    #print(r.content)

    html=r.content.decode('utf-8')
    soup=BeautifulSoup(html,'lxml')
    all_info=soup.find("ul",class_="for-list")
    all_theme_tag=all_info.find_all("li")



    data_list=[]
    for theme_tag in all_theme_tag:
        name_tag=theme_tag.find("a",class_="truetit")
        name=name_tag.text
        link=name_tag['href']
        link='http://bbs.hupu.com'+link

        author_tag=theme_tag.find("a",class_="aulink")
        author_name=author_tag.text
        author_link=author_tag['href']
        built_time=theme_tag.find("div",class_="author box").contents[5].text.strip()
        
        rep_view_tag=theme_tag.find("span",class_="ansour box")
        rep_text_list=rep_view_tag.text.split('/')
        reply_num=rep_text_list[0].strip()
        view_num=rep_text_list[1].strip()

        lastest_tag=theme_tag.find("div",class_="endreply box")
        lastest_anthor=lastest_tag.span.text
        lastest_reply_time=lastest_tag.a.text
        lastest_reply_time=modify_time(lastest_reply_time)

        data_list.append([name,link,author_name,author_link,built_time,reply_num,
        view_num,lastest_anthor,lastest_reply_time])


    for row in data_list:
        connection.update(
            {'link':row[1]},#primary key
            {
                'title':row[0],
                'author_name':row[2],
                'author_link':row[3],
                'built_time':row[4],
                'reply_num':row[5],
                'view_num':row[6],
                'lastest_author':row[7],
                'lastest_reply_time':str(row[8]),
            }
        )
    time.sleep(3)
    print("第"+str(i)+'页over!')








