# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BlogspiderPipeline:
    file_path="c:/users/林/desktop/python_item/spider/blogspider/output.text"
    def __init__(self):
        self.f=open(self.file_path,'a+',encoding='utf-8')
    def process_item(self, item, spider):
        title=item['title']
        link=item['link']
        content=item['content']
        output_text=title+'\t'+link+'\t'+content+'\n\n'
        self.f.write(output_text)
        return item
