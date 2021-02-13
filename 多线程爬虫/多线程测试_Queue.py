import threading
import time
import queue 
import requests

class QueueThread(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.name=name
        self.q=q

    def run(self):
        while not q.empty():
            print(q.qsize(),self.name,end=' ')
            visit_website(self.q)


def visit_website(q):
    url=q.get(timeout=2)
    headers={
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    }
    try:
        r=requests.get(url,headers=headers,timeout=3)
        print(r.status_code,url)
    except Exception as e:
        print("error:",e)

link_list=[]
filepath="site_rank.txt"
with open(filepath,'r') as f:
    file_list=f.readlines()
    for row in file_list:
        link=row.replace('\n','')
        link_list.append(link)

q=queue.Queue(1000)
for i in link_list:
    q.put(i)

#创建5个线程名
thread_name_list=['THREAD_'+str(i) for i in range(1,6)]
thread_list=[]
st=time.time()
for th_name in thread_name_list:
    th=QueueThread(th_name,q)
    th.start()
    thread_list.append(th)
for th in thread_list:
    th.join()
ed=time.time()
print('spend:',ed-st)
    

