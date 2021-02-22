from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import re

executable_path=r'C:\Users\林\Desktop\chromedriver.exe'
drive=webdriver.Chrome(executable_path=executable_path)


def get_bookname_and_reviewlink(file_name):
    name_link_list=[]
    with open(file_name,encoding='utf-8') as f:
        reader=csv.reader(f)
        f=1
        for row in reader:
            
            if row!=[] and f==0:
               name_link_list.append([row[1],row[-2]])
            if f==1:
                    f-=1
       
    return name_link_list


def save_comment_info(original_url,save_file_name,book_name):
    '''获取单一url所有评论'''
    temp_list=[]
    index=1
    pos=original_url.find('?')
    url0=original_url[:pos+1]
    
    while 1:
        #time.sleep(2)
        url=url0+"pageNumber="+str(index)
        print("url",url)
        try:
            drive.get(url)
            soup=BeautifulSoup(drive.page_source,'lxml')
            div_tag=soup.find('div',id="cm_cr-review_list")
            
            try:
                break_text=soup.find("div",class_="a-section a-spacing-top-large a-text-center no-reviews-section").span.text
                if break_text=="抱歉，无评论满足您当前的筛选条件。":
                        break
            except:
                pass
            

            for each_tag in div_tag.find_all('div',class_="a-section review aok-relative"):
                try:
                    reviewer=each_tag.find("span",class_="a-profile-name").text
                    star=each_tag.find("a",class_="a-link-normal")["title"].split(".")[0]
                    head=each_tag.find("a",class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold").span.text
                    content=each_tag.find("span",class_="a-size-base review-text review-text-content").span.text
                    temp_list.append([reviewer,star,head,content])
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        index+=1
    try:
        with open(save_file_name,'a+',newline="",encoding='utf-8') as f:
            writer=csv.writer(f)
            writer.writerows(temp_list)
    except Exception as e:
        print(e)

def parse_and_save(file_name):
    name_link_list=get_bookname_and_reviewlink(file_name)
    for each in name_link_list:
        book_name,review_link=each[0],each[1]
        save_comment_info(review_link,"reviews/"+book_name+"_reviews.csv",book_name)



parse_and_save("传记_rank.csv")

