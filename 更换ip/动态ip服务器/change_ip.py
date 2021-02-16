import os
import time

class Asdl:
    '''连接和断开拨号服务器'''
    def __init__(self):
        self.name='宽带连接'
        self.username="usdsf"
        self.password="123456"

    def connect(self):
        cmd_str=f"rasdial {self.name} {self.username} {self.password}"
        os.system(cmd_str)
        time.sleep(5)
    
    def disconnect(self):
        cmd_str=f"rasdial {self.name} \disconnect"
        os.system(cmd_str)
        time.sleep(5)

    def reconnect(self):
        self.disconnect()
        self.connect()

if __name__=='__main__':
    asdl=Asdl()
    asdl.connect()