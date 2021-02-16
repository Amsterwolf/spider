import requests
import re
from http import cookiejar
'''爬虫登录github'''

def parse_and_login(username,password):
    login_url='https://www.github.com/login'
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

    }

    session=requests.Session()
    session.cookies=cookiejar.LWPCookieJar('cookies')
    r_login=session.get(login_url,headers=headers)
    html=r_login.content.decode('utf-8')
    

    #解析提交参数
    pattern=re.compile('<input type="hidden" name="authenticity_token" value="(.*?)" />')
    auth_token=pattern.findall(html)[0]
    print('auto_token:',auth_token)
    pattern_timestamp=re.compile('<input type="hidden" name="timestamp" value="(.*?)" class="form-control" />')
    timestamp=pattern_timestamp.findall(html)[0]
    print('timestamp:',timestamp)
    pattern_timestamp_secret=re.compile('<input type="hidden" name="timestamp_secret" value="(.*)" class="form-control" />')
    timestamp_secret=pattern_timestamp_secret.findall(html)[0]
    print('timestamp_secret:',timestamp_secret)


    session_url='https://github.com/session'
    data={
        'commit':'Sign in',
        'authenticity_token':auth_token,
        'login':username,
        'password':password,
        
        #'webauthn-support':'supported',
        #'webauthn-iuvpaa-support': 'supported',
    
        'timestamp':timestamp,
        'timestamp_secret':timestamp_secret,
        

        

    }

    r_session=session.post(session_url,data=data,headers=headers)#,cookies=cookies)
    if r_session.status_code==200:
        print("登录成功")
    #print(r3.content.decode('utf-8'))

    session.cookies.save()
