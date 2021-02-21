import threading
import requests
import re
import queue
import time



def modify_url(url):
    if url[0]=='/':
        url='https://www.wiki-wiki.top'+url
    return url

def scrapy_BFS(st_url,max_depth=2,max_threadnum=5):
    #爬取链接数
    count=0
    #待爬队列
    q=queue.Queue()
    crawled_url_list=[]
    #tuple结构，记录深度
    q.put((st_url,1))
    
    crawled_url_list.append(st_url)

    thread_list=[]
    #多线程
    for i in range(max_threadnum):
        t=threading.Thread(name="Thread_"+str(i+1),target=target,args=(q,max_depth,crawled_url_list,count))
        thread_list.append(t)
        t.start()
    
    
 
    for t in thread_list:
        t.join()



    


def target(q,max_depth,crawled_url_list,count):
    while 1:
        print(threading.current_thread().name)
        time.sleep(1)
if __name__=='__main__':
    con=threading.Condition()
    scrapy_BFS("https://www.wiki-wiki.top/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")


  
        



