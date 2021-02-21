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
    count=1
    #待爬队列
    q=queue.Queue()
    crawled_url_list=[]
    #tuple结构，记录深度
    q.put((st_url,1))
    
    crawled_url_list.append(st_url)

    thread_list=[]
    #多线程
    for i in range(10):
        t=threading.Thread(name="Thread_"+str(i+1),target=target,args=(q,max_depth,crawled_url_list,count))
        thread_list.append(t)
        t.start()
        #防止触发while条件
        if i==0:
            time.sleep(10)
    
    
 
    for t in thread_list:
        t.join()



    


def target(q,max_depth,crawled_url_list,count):
    #threading.current_thread().name
    while not q.empty():
        #出队
        url_tuple=q.get()
        url=url_tuple[0]
        deep=url_tuple[1]
        if deep>max_depth:
            break
        
        
        try:
            headers={
                'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

            }
            r=requests.get(url,headers=headers,timeout=3)
            if r.status_code!=200:
                raise Exception
        except Exception as e:
            print("error:",e)
        else:
            url_list0=re.findall('<a href="(.*?)".*?</a>',r.text)
            for suburl in url_list0:
                suburl=modify_url(suburl)
                if suburl not in crawled_url_list:
                    con.acquire()
                    #记录入过队
                    crawled_url_list.append(suburl)
                    #入队
                    q.put((suburl,deep+1))
                    
                    
                    msg=f"{threading.current_thread().name}\tNo.{count}\tqsize:{q.qsize()}\tDeep:{deep}\tWay:{url} -> {suburl}"
                    print(msg)

                    try:
                        with open("wiki_url_BFS.txt",'a+') as f:
                            f.write(msg+'\n',)
                        count+=1
                    except Exception as e:
                        print(e)
                    
                    con.release()
                    
if __name__=='__main__':
    con=threading.Condition()
    scrapy_BFS("https://www.wiki-wiki.top/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")


  
        



