# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from moneynews_spider.items import MoneynewsSpiderItem
class MoneynewsSpider(scrapy.Spider):
    name = 'moneynews'
    allowed_domains = ['finance.eastmoney.com']
    start_urls = ['http://finance.eastmoney.com/a/cywjh.html']
   
    headers={
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

    }

    def start_requests(self):
        #爬取前十页
        for i in range(1,11):
            url='http://finance.eastmoney.com/a/cywjh_'+str(i)+'.html'
            
            print("当前页面是：",url)
            yield scrapy.Request(url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        soup=BeautifulSoup(response.text,'lxml')
        p_tag_list=soup.find_all("p",class_="title")
        a_tag_list=[p.a for p in p_tag_list]
        for a in a_tag_list:
            title=a.text.strip()
            link=a["href"]
            print(title+'\n'+link)

            item=MoneynewsSpiderItem()
            item["title"]=title
            item["link"]=link
            yield scrapy.Request(link,callback=self.parse2,headers=self.headers,meta={'item':item},dont_filter=True)#开放域名限制
    
    def parse2(self,response):
        item=response.meta['item']
        soup=BeautifulSoup(response.text,'lxml')
        content=soup.find("div",id="ContentBody").text.strip().replace('\n',' ')
        item["content"]=content
        return item


