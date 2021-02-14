import json
str1="我们ai你们"
with open('ajson.json','w',encoding='utf-8') as f:
    json.dump(str1,f,ensure_ascii=False)#可以以非ascii码解析