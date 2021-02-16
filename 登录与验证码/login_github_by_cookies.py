import requests
from http.cookiejar import LWPCookieJar

def is_login():
    '''检测是否登录'''
    session=requests.session()
    session.cookies=LWPCookieJar('cookies')
    try:
        session.cookies.load(ignore_discard=True)
    except Exception as e:
        print("cookies加载失败")
        print("error:",e)
        return False

    test_login_url='https://github.com/settings/profile'
    headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

    }
    r=session.get(test_login_url,headers=headers,allow_redirects=False)#禁止重定向
    '''history_list=r.history
    for history in history_list:
        #print(history.headers)
        print(history.headers['location'])#历史重定向url'''

    if r.status_code==200:
        return True
    return False

if __name__=='__main__':
    if is_login():
        print("已登录")
    else:
        print("未登录")