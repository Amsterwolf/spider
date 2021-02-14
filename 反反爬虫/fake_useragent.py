
import requests
import json
import random

'''伪装请求头'''

with open('fake_ua.json','r') as f:
    fake_ua_list=json.load(f)

url='http://www.baidu.com'
ua=random.choice(fake_ua_list)
headers={
    'user-agent':ua
}
r=requests.get(url,headers=headers)
print(r.status_code)
print(r.request.headers)

