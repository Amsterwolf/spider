import requests
import json
import pymysql
'''从百度地图api获取数据存入mysql'''
#连接数据库
db=pymysql.connect(host="127.0.0.2",user="root",password="123",database="baidumap")
#创建光标
cursor=db.cursor()

city_list=[]

def getjson(region,page_num=0):
    '''调用api接口查询'''
    url="https://api.map.baidu.com/place/v2/search"
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

    }
    params={
        "q":"公园",
        "region":region,
        "page_num":page_num,
        "output":'json',
        'ak':"n4xwO6aIwWxIgcsfBHvL7O7iYms0oUvo"
    }
    r=requests.get(url=url,headers=headers,params=params)
    #print(r.url)
    decodejson=json.loads(r.text)
    return decodejson

def getjson2(uid):
    '''查询详细信息返回decodejson'''
    url="https://api.map.baidu.com/place/v2/detail"
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

    }
    params={
        "uid":uid,
        "output":'json',
        'ak':"n4xwO6aIwWxIgcsfBHvL7O7iYms0oUvo",
        'scope':2,
    }
    r=requests.get(url=url,headers=headers,params=params)
    #print(r.url)
    decodejson=json.loads(r.text)
    return decodejson

def get_name_and_num():
    '''获取各省（区）对应的公园数，存入txt及列表'''
    decodejson=getjson("全国")
    results_list=decodejson['results']
    if results_list==[]:
        return
    for result in results_list:
        name=result['name']
        num=result['num']
        output=f"{name}\t{num}\n"
        global city_list
        city_list.append(name)
        with open('citys.txt','a+',encoding='utf-8') as  f:
            f.write(output)

def creat_new_table_city():
    try:
        command='''CREATE TABLE baidumap.city (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            location_lat FLOAT NOT NULL,
            location_lng FLOAT NOT NULL,
            address VARCHAR(100) NOT NULL,
            street_id VARCHAR(100) ,
            telephone VARCHAR(45),
            uid VARCHAR(100) ,
            creat_time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id));'''
        cursor.execute(command)
        db.commit()
    except Exception as e:
        print(e)
    #db.close()

def creat_new_table_parkinfo():
    '''可通过Mysql Workbeach 创建,存储公园的详细信息'''
    pass

def insert_to_table_city(city_list):
    '''添加公园的粗略信息至table city'''
    for city in city_list:
        page_num=0
        while 1:
            decodejson=getjson(city,page_num=page_num)
            results_list=decodejson['results']
            if results_list==[]:
                break
            for result in results_list:
                street_id,telephone,uid=None,None,None
                try:
                    name=result['name']
                    location_lat=result['location']['lat']
                    location_lng=result['location']['lng']
                    address=result['address']
                    street_id=result['street_id']
                    telephone=result['telephone']
                    uid=result['uid']
                except:
                    pass
                else:
                    command=f'''INSERT INTO baidumap.city (name, location_lat, location_lng, address, street_id, telephone, uid) 
                    VALUES ('{name}','{location_lat}','{location_lng}','{address}', '{street_id}', '{telephone}', '{uid}');'''
                    #print(command)
                    cursor.execute(command)
                    db.commit()

            page_num+=1


def insert_to_table_parkinfo(uid_list):
    '''通过uid添加公园的详细信息至table parkinfo'''
    for uid in uid_list:
        decodejson=getjson2(uid)

        results_list=decodejson["result"]
        
        for result in results_list:
            street_id,telephone,uid,tag,shop_hours,alias,detail_url,tpye,overall_rating,\
            image_num,comment_num,content_tag,detail=None,None,None,None,None,None,\
            None,None,None,None,None,None,None
            try:
                name=result['name']
                location_lat=result['location']['lat']
                location_lng=result['location']['lng']
                address=result['address']
                street_id=result['street_id']
                telephone=result['telephone']
                uid=result['uid']
                detail_info=result['detail_info']
                tag=detail_info['tag']
                shop_hours=detail_info['shop_hours']
                alias=detail_info['alias']
                detail_url=detail_info['detail_url']
                tpye=detail_info['tpye']
                overall_rating=detail_info['overall_rating']
                image_num=detail_info['image_num']
                comment_num=detail_info['comment_num']
                content_tag=detail_info['connent_tag']
                detail=detail_info['detail']
                
            except Exception as e:
                print(e)
            else:
                command=f'''INSERT INTO baidumap.parkinfo (name, location_lat, location_lng, address, street_id, telephone, \
                uid,tag,shop_hours,alias,detail_url,tpye,overall_rating,image_num,comment_num,content_tag,detail) 
                VALUES ('{name}', '{location_lat}', '{location_lng}', '{address}', '{street_id}', '{telephone}','{uid}','{tag}',\
                '{shop_hours}','{alias}','{detail_url}','{tpye}','{overall_rating}','{image_num}','{comment_num}','{content_tag}','{detail}');'''
                #print(command)
                cursor.execute(command)
                db.commit()

       

def get_uid_from_db():
    '''从数据库查找uid,并返回uid_list'''
    command="select uid from baidumap.city where id>0"
    cursor.execute(command)
    db.commit()
    results=cursor.fetchall()
    #print(results)
    uid_list=[]
    for row in results:
        uid_list.append(row[0])
    #print(uid_list)
    return uid_list

#test_list=["cdf5ad59d3519e498bfc066c"]
#insert_to_table_parkinfo(test_list)

get_name_and_num()
creat_new_table_city()
insert_to_table_city(city_list)
insert_to_table_parkinfo(get_uid_from_db())

cursor.close()
db.close()
