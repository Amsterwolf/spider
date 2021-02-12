# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoneynewsSpiderPipeline:
    
    def __init__(self):
        self.path="c:/users/林/desktop/python_item/spider/moneynews_spider/output_news.txt"
        self.f=open(self.path,'w',encoding='utf-8')

    def process_item(self, item, spider):
        title=item['title']
        link=item['link']
        content=item['content']
        text=title+'\t'+link+'\t'+content+"\n\n"
        self.f.write(text)
        return item
