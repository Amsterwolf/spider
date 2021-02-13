from multiprocessing import cpu_count,Process,Queue
import time
import requests
#print(cpu_count())

class AProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q=q
        
    def run(self):
        print("Start process:",self.name)
        while not self.q.empty():
            print(self.q.qsize(),self.name,end=' ') 
            visit_website(self.q)
        print("End process:",self.name)

def visit_website(q):
    url=q.get(timeout=2)
    try:
        headers={
            "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

        }
        r=requests.get(url,headers=headers,timeout=3)
        print(r.status_code,url)
    except Exception as e:
        print("error:",e,url)

if __name__=='__main__':#防止子进程无限递归
    filepath="site_rank.txt"
    link_list=[]
    with open(filepath,'r') as f:
        file_list=f.readlines()
        for row in file_list:
            link=row.replace('\n','')
            link_list.append(link)

    q=Queue(1000)
    for i in link_list:
        q.put(i)

    
    st=time.time()
    process_list=[]
    for i in range(8):#八进程
        pro=AProcess(q)
        pro.daemon=True
        pro.start()#向操作系统发送一个请求，操作系统会申请内存空间给，然后把父进程的数据拷贝给子进程，作为子进程的初始数据。
        process_list.append(pro)

    for pro in process_list:
        pro.join()
    ed=time.time()
    print("Process+Queue 多进程爬虫的时间为：",ed-st)
