import requests
from bs4 import BeautifulSoup
import chardet

url="https://www.sina.com.cn/"
headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
r=requests.get(url,headers=headers)
after_gzip=r.content
charset=chardet.detect(after_gzip)['encoding']#此处charset='utf-8'
print("解压后字符串的编码：",charset)
print(after_gzip.decode(charset))


