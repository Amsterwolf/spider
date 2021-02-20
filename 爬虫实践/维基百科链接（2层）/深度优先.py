import requests
import re
import time

'''爬取中文维基百科网的两层链接'''
count=0
crawled_url_list=[]

def modify_url(url):
    if url[0]=='/':
        url='https://www.wiki-wiki.top'+url
    return url

def scrapy(url,deep=1):
    #全局变量
    global count
    url=modify_url(url)

    if url not in crawled_url_list:
        crawled_url_list.append(url)
        
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    }
    try:
        r=requests.get(url,headers=headers,timeout=5)
        print("text:",r.text[:30])
    except Exception as e:
        print("爬取失败",e)
        return 
    link_list=re.findall('<a href="(.*?)".*?</a>',r.text)
    for link in link_list:
        link2=modify_url(link)
        if link!=link2:
            link_list.remove(link)
            link_list.append(link2)

    wait_to_crawl_list=list(set(link_list)-set(crawled_url_list))
    for suburl in wait_to_crawl_list:
        count+=1
        msg=f"No.{count}\tDeep:{deep}\tWay:{url} -> {suburl}"
        with open("wiki_url.txt",'a+') as f:
            f.write(msg+'\n')
            
        
        if deep<2:
            scrapy(suburl,deep+1)

if __name__=="__main__":
    scrapy('https://www.wiki-wiki.top/wiki/Wikipedia:%E9%A6%96%E9%A1%B5')

        

    