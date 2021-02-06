import requests
from bs4 import BeautifulSoup
link='http://httpbin.org/post'
key_dic={
    'key1':'val1',
    'key2':'val2',
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    
}
data={
    'k1':'v1',
    'k2':'v2',
}
#r=requests.get(link,params=key_dic,headers=headers)
r=requests.post(link,data=data,headers=headers,timeout=1)
print('r.url:',r.url)
print("r.encoding:",r.encoding)
print("r.status_code:",r.status_code)
#print('r.content:',r.content[:100])
print()
print("r.text:",r.text[:100])


