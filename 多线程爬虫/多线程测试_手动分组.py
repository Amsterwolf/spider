import threading
import time
import requests
class MyThread(threading.Thread):
    def __init__(self,name,link_range):
        threading.Thread.__init__(self)
        self.name=name
        self.link_range=link_range
    def run(self):
        print("Start:",self.name)
        visit_website(self.name,self.link_range)
        print("End:",self.name)

def visit_website(thread_name,link_range):
    for i in range(link_range[0],link_range[1]):
        url=link_list[i]
        headers={
            "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        }
        print("THREAD:",thread_name,end=" ")
        try:
            r=requests.get(url,headers=headers,timeout=3)
            print(r.status_code,url)
        except Exception as e:
            print("Error:",e)
        

filepath="site_rank.txt"

link_list=[]
with open(filepath,'r') as f:
    file_list=f.readlines()
    for row in file_list:
        link=row.replace('\n','')
        link_list.append(link)
link_range_list=[(0,200),(200,400),(400,600),(600,800),(800,1000)]
thread_list=[]
st=time.time()
for i in range(1,6):
    th=MyThread('thread_'+str(i),link_range_list[i-1])
    th.start()#开始一线程
    thread_list.append(th)

for th in thread_list:
    th.join()#wait
ed=time.time()
print("finished project,spend:",ed-st)