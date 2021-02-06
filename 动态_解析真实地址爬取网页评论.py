import requests
from bs4 import BeautifulSoup
import json

def  get_single_page_comment(url):
    #print("url:",url)
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        #'host':'api-zero.livere.com',
    }
    #url="https://api-zero.livere.com/v1/comments/list?callback=jQuery112405231158605050379_1612618753162&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1612618753164"

    r=requests.get(url,headers=headers)
    print("r.status_code:",r.status_code)
    #print(r.text[:100])
    st=r.text.find('{')
    json_str=r.text[st:-2]

    #with open("comment_data.json",'w') as f:
        #f.write(json_str)#生成json文件以供分析
    json_dic=json.loads(json_str)#json字符串字典化
    comments_list=json_dic['results']['parents']
    
    get_comments_list=[]
    for dic in comments_list:
        comment=dic['content']
        get_comments_list.append(comment)
    return get_comments_list



with open("all_comments.txt",'w') as f:
    for i in range(1,5):
        url=f'''https://api-zero.livere.com/v1/comments/list?callback=jQuery11240040314063237201436_
1612621180531&limit=10&offset={i}&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020
&livereSeq=28583&smartloginSeq=5154&code=&_=1612621180537'''
        comments_list=get_single_page_comment(url)
        for i in comments_list:
            f.write(i)#写入每条评论至all_comments.txt
            f.write('\n')
        