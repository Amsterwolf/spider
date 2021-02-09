import requests
from bs4 import BeautifulSoup

def get_movie_list():
    movie_list=[]
    headers={
            'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            'host':'movie.douban.com'
        }
    for i in range(0,10):
        url="http://movie.douban.com/top250"#+f"?start={i*25}"
        params={
            "start":f'{i*25}',

        }
        r=requests.get(url,headers=headers,params=params,timeout=10,allow_redirects=False)
        soup=BeautifulSoup(r.text,'html.parser')
        print("page num:",i+1)
        print("r.url:",r.url)
        print("r.status_code:",r.status_code)
        #print("r.text:",r.text[:100])
        try:
            title=soup.find_all('span',class_='title').text
        except:
            pass
        else:
            print(title)
            movie_list.append(title)
    
    return movie_list

movies=get_movie_list()
print(movies)



