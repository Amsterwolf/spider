import requests
from bs4 import BeautifulSoup
from PIL import Image
import os

'''人工识别验证码'''

post_url="http://www.santostang.com/wp-login.php?action=register"
headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

    }

def get_captcha(session):
    r=session.get(post_url,headers=headers)
    soup=BeautifulSoup(r.text,'lxml')
    captcha_url=soup.find('img',id="captcha_code_img")['src']
    r=session.get(captcha_url,headers=headers)
    #保存验证码图片
    with open('captcha.jpg','wb') as f:
        f.write(r.content)
    try:
        #pillow库打开
        image=Image.open('captcha.jpg')
        image.show()
        image.close()
    except:
        #手动打开
        print(f"请到{os.path.abspath('captha.jpg')}目录找到captcha.jpg手动输入")
    
    return input("please input the captcha\n>")
    


def register(username,useremail,session):
    data={
        "user_login":username,
        "user_email":useremail,
        "ux_txt_captcha_challenge_field":get_captcha(session),
    }
    r=session.post(post_url,headers=headers,data=data)
    if r.status_code==200:
        try:
            error=BeautifulSoup(r.text,'lxml').find("div",id="login_error").text
            print(error)
        except:
            return True
        
    return False

if __name__=='__main__':
    session=requests.session()
    username="aadfdfdffda"
    useremail="123456789@qq.com"
    if register(username,useremail,session):
        print("注册成功")
    else:
        print("注册失败")