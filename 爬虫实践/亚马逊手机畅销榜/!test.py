from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import re

executable_path=r'C:\Users\林\Desktop\chromedriver.exe'
drive=webdriver.Chrome(executable_path=executable_path)


def parse_soup(soup,file_name):
    ol_tag=soup.find("ol",id="zg-ordered-list")
    book_list=[]
    book_list.append(['rank','title','link','author','star','comment_num','comment_link','price'])
    for li_tag in ol_tag.find_all("li",class_="zg-item-immersion"):
        try:
            rank=li_tag.find("span",class_="zg-badge-text").text.replace("#","")
            title=li_tag.find("div",class_="p13n-sc-truncate-desktop-type2 p13n-sc-truncated").text
            link="https://www.amazon.cn"+li_tag.find("a",class_="a-link-normal")['href']
            author=li_tag.find("span",class_="a-size-small a-color-base").text
            star=li_tag.find("span",class_="a-icon-alt").text.split(" ")[1]
            comment_num=ol_tag.find("a",class_="a-size-small a-link-normal").text
            comment_link="https://www.amazon.cn"+ol_tag.find("a",class_="a-size-small a-link-normal")['href']
            price=ol_tag.find("span",class_="p13n-sc-price").text
        
            #print(rank,title,link,author,star,comment_num,comment_link,price)
            book_list.append([rank,title,link,author,star,comment_num,comment_link,price])
        except Exception as e:
            print(e)
    with open(f"{file_name}.csv",'a',encoding='utf-8') as f:
        write=csv.writer(f,dialect='excel')
        write.writerows(book_list)

def parse_soup_for_type(soup):
    ul_tag=soup.find("ul",id="zg_browseRoot").ul.ul.ul
    type_list=[]
    for li_tag in ul_tag.find_all("li"):

        try:
            a_tag=li_tag.a
            type_name=a_tag.text
            
            type_link_id=re.findall(r"https://.*?/([0-9]+)/.*?",a_tag["href"])[0]
            type_link="https://www.amazon.cn/gp/bestsellers/digital-text/"+type_link_id+"/ref=zg_bs_pg_2?ie=UTF8&pg=1"
            type_list.append([type_name,type_link])
        except Exception as e:
            print(e)
    
    return type_list

def get_csv_file(url,file_name):
    
    drive.get(url)
    soup=BeautifulSoup(drive.page_source,'lxml')
    parse_soup(soup,file_name)

def get_type_list(url):
    drive.get(url)
    soup=BeautifulSoup(drive.page_source,'lxml')
    tpye_list=parse_soup_for_type(soup)
    return tpye_list



url="https://www.amazon.cn/gp/bestsellers/digital-text/116169071/ref=zg_bs_pg_1?ie=UTF8&pg=1"
'''for i in range(1,3):
    url=url[:-1]+str(i)
    get_csv_file(url)'''

type_list=get_type_list(url)
#print(type_list)
for eachtype in type_list:
    type_name,url=eachtype[0],eachtype[1]
    for i in range(1,3):
        url=url[:-1]+str(i)
        get_csv_file(url,type_name+"_rank")


#https://www.amazon.cn/gp/bestsellers/digital-text/144154071/ref=zg_bs_nav_kinc_2_116169071
#https://www.amazon.cn/gp/bestsellers/digital-text/144154071/ref=zg_bs_pg_2?ie=UTF8&pg=2