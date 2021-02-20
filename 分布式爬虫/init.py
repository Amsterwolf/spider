import json

with open("site_rank.txt",'r') as f:
    
    rows_list=f.readlines()
    urls_list=[]
    for row in rows_list:
        url=row.replace('\n','')
        urls_list.append(url)
    f2=open("sites.json",'w')
    json.dump(urls_list,f2)
    f2.close()
