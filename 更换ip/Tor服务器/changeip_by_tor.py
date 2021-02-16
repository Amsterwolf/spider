from stem import Signal
from stem.control import Controller
import socket
import socks
import requests
import time

#使用9151端口
controller=Controller.from_port(port=9151)
controller.authenticate()
#Tor使用9150端口为默认的socks端口
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9150)
socket.socket=socks.socksocket

total_scrapy_time=0
total_changeip_time=0

for i in range(1,11):
    #获取ip地址的网站
    r=requests.get("https://checkip.amazonaws.com")
    print(f"第{i}次ip:",r.text)

    #爬取网页计时
    st1=time.time()
    r=requests.get("https://www.baidu.com")
    print(r.status_code)
    ed1=time.time()
    total_scrapy_time+=ed1-st1
    print(f"第{i}次爬取花费时间：",ed1-st1)

    #更换ip计时
    st2=time.time()
    controller.signal(Signal.NEWNYM)
    ed2=time.time()
    time.sleep(5)
    total_changeip_time+=ed2-st2
    print(f"第{i}次爬取花费时间：",ed2-st2)

print("平均爬取网页时间：",total_scrapy_time/10)
print("平均更换ip时间：",total_changeip_time/10)
    