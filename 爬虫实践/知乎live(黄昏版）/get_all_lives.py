import requests
import json
import time
import random
from pymongo import MongoClient
'''获取live信息，并获取相关live听众的信息，存储于mongodb'''
client=MongoClient('localhost',27017)
db=client.zhihu_db
collection=db.live


def scrapy(url):
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

    }
    r=requests.get(url,headers=headers)
    return r.text

def insert_to_collection():
    url="https://api.zhihu.com/lives/homefeed"

    is_end=False
    while not is_end:
        html=scrapy(url)
        #print(html)
        decodejson=json.loads(html)
        collection.insert_one(decodejson)
        #print(decodejson)
        next_page=decodejson['paging']['next']
        is_end=decodejson['paging']['is_end']
        #print(next_page)
        #print(is_end)
        url=next_page
        time.sleep(random.uniform(2.0,5.0))

def find_live_id():
    all_live_id_list=[]
    records_list=collection.find()
    datas_list=[record['data'] for record in records_list] 
    for data_dic_list in datas_list:
        for data_dic in data_dic_list:
            id=data_dic['id'][4:]
            #print(id)
            all_live_id_list.append(id)
    return all_live_id_list
    


def get_audience(live_id):
    url="https://api.zhihu.com/lives/"+live_id+'/members'
    is_end=False
    while not is_end:
        html=scrapy(url)
        decodejson=json.loads(html)
        decodejson['live_id']=live_id
        db.live_audience.insert_one(decodejson)
        url=decodejson['paging']['next']
        is_end=decodejson['paging']['is_end']



live_id_list=find_live_id()
first_id=live_id_list[0]
get_audience(first_id)