'''import _thread
import time

def print_time(threadname,delay):
    cot=0
    while cot<3:
        time.sleep(delay)
        print(threadname,time.ctime(time.time()))
        cot+=1

_thread.start_new_thread(print_time,('thread_1',1))
_thread.start_new_thread(print_time,('thread_2',2))
while 1:
    pass'''

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=delay
    def run(self):
        print("Start thread:",self.name)
        self.print_time(self.name,self.delay)
        print("End thread:",self.name)
    
    def print_time(self,name,delay):
        cot=0
        while cot<3:
            time.sleep(delay)
            print(name,time.ctime())
            cot+=1

th1=MyThread('thread_1',1)
th2=MyThread('thread_2',2)
th1.start()
th2.start()
th1.join()
th2.join()
print("end main thread")
