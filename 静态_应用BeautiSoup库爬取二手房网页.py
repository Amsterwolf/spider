import requests
from bs4 import BeautifulSoup
import csv
#爬取前10页
f=open(r'data_saver/二手房信息.csv','w',newline='')
writer=csv.writer(f)
for i in range(1,11):
    url='https://hangzhou.anjuke.com/sale/p'+str(i)+'/'
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

    }

    r=requests.get(url,headers=headers)
    #print(r.text[:100])
    soup=BeautifulSoup(r.text,'lxml')
    house_list=soup.find_all("div",class_="property-content")
    for house in house_list:
        name=house.find("p",class_="property-content-info-comm-name").text.strip()
        addr=house.find("p",class_="property-content-info-comm-address").text
        info=house.find("h3",class_="property-content-title-name").text.strip()
        #print(name)
        price=house.find("span",class_="property-price-total-num").text.strip()
        price_unit=house.find("span",class_="property-price-total-text").text
        ave_price=house.find("p",class_="property-price-average").text
        content_info_tag=house.find("div",class_="property-content-info")
        '''print(content_info_tag.prettify())
        for i in range(len(content_info_tag.contents)):
            print("i=:",i,content_info_tag.contents[i])'''
        room_num=content_info_tag.contents[0].text.strip().replace(" ","")
        square_meter=content_info_tag.contents[2].text.strip()
        floors=content_info_tag.contents[6].text.strip()
        tags_list=house.find_all("span",class_="property-content-info-tag")
        tags=[i.text for i in tags_list]
        writer.writerow([f"page{i}",name,addr,info,price,price_unit+ave_price,room_num,square_meter,floors,tags])
        

f.close()