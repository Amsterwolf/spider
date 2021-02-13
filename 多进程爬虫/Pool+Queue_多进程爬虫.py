from multiprocessing import Pool,Manager
import time
import requests

def visit_website2(q,index):
    while not q.empty():
        url=q.get(timeout=2)
        pro_name="process_"+str(index)
        try:
            headers={
                "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

            }
            r=requests.get(url,headers=headers,timeout=3)
            print(q.qsize(),pro_name,r.status_code,url)
        except Exception as e:
            print(q.qsize(),pro_name,"error:",e,url)

if __name__=='__main__':#防止子进程无限递归

    manager=Manager()
    q=manager.Queue(1000)

    filepath="site_rank.txt"
    link_list=[]
    with open(filepath,'r') as f:
        file_list=f.readlines()
        for row in file_list:
            link=row.replace('\n','')
            link_list.append(link)

    #填充队列
    for i in link_list:
        q.put(i)

    pool=Pool(processes=8)#上限八进程
    st=time.time()
    for i in range(1,10):#10个创造子进程请求
        pool.apply_async(visit_website2,(q,i))
    
    print("start program")
    pool.close()
    pool.join()#阻塞
    
   

 
    ed=time.time()
    print("Pool+Queue 多进程爬虫的时间为：",ed-st)
