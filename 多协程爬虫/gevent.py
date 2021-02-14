import gevent
from gevent.queue import Queue,Empty
import time
import requests
from gevent import  monkey
#将IO转为异步执行的函数
monkey.patch_all()

def visit_website(q,index):
    while not q.empty():
        url=q.get(timeout=2)
        pro_name="process_"+str(index)
        try:
            headers={
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

            }
            r=requests.get(url,headers=headers,timeout=3)
            print(q.qsize(),pro_name,r.status_code,url)
        except Exception as e:
            print(q.qsize(),pro_name,"error:",e,url)

def boss():
    for i in link_list:
        q.put_nowait(i)

if __name__=='__main__':#防止子进程无限递归

    filepath="site_rank.txt"
    link_list=[]
    with open(filepath,'r') as f:
        file_list=f.readlines()
        for row in file_list:
            link=row.replace('\n','')
            link_list.append(link)

    #填充队列
    q=Queue(1000)
    gevent.spawn(boss).join()

    st=time.time()
    #创建子进程
    jobs=[]
    for i in range(10):
        jobs.append(gevent.spawn(visit_website,(q,i+1)))
    gevent.joinall(jobs)

    
    

    ed=time.time()
    print("gevent+Queue 多进程爬虫的时间为：",ed-st)

