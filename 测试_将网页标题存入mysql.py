import requests
from lxml import etree
import pymysql

#连接数据库scraping
db=pymysql.connect(host="127.0.0.2",user="root",password="123",database="scraping")
#创建光标
cursor=db.cursor()

url="http://www.santostang.com/"
headers={
    "usr_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

}
r=requests.get(url,headers=headers)

html=etree.HTML(r.text)
tag_list=html.xpath('//*[@id="main"]/div/div/article/header/h1/a')
#print(tag_list)
for tag in tag_list:
    url=tag.xpath('@href')[0]
    #print(url)
    content=tag.xpath('text()')[0]
    #print(content)

    #执行sql语句
    sql=f"insert into urls (url,content) values ('{url}','{content}') "
    cursor.execute(sql)

db.commit()
db.close()
