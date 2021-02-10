# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from blogspider.items import BlogspiderItem

class TostangSpider(scrapy.Spider):
    name = 'tostang'
    allowed_domains = ['www.santostang.com']
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        #print(response.text)
        soup=BeautifulSoup(response.text,'lxml')
        h1_list=soup.find_all("h1",class_="post-title")
        items=[]
        for i in range(len(h1_list)):
            title=h1_list[i].a.text
            link=h1_list[i].a['href']
            
            #封装数据
            item=BlogspiderItem()#字典数据类型
            item['title']=title
            item['link']=link
            yield scrapy.Request(link,callback=self.parse2,meta={"item":item})
        
    
    def parse2(self,response):
        item=response.meta['item']
        soup=BeautifulSoup(response.text,'lxml')
        content=soup.find("div",class_="view-content").text.strip().replace('\n',' ')
        item['content']=content
        return item
        
        
