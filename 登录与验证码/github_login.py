import requests
import re

home_url='https://github.com/'
headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

}
session=requests.Session()
r=session.get(home_url,headers=headers)
html=r.content.decode('utf-8')

pattern=re.compile('<input type="hidden" data-csrf="true" name="authenticity_token" value="(.*)" />')
auth_token=pattern.findall(html)[0]
print('auto_token:',auth_token)

login_url='https://www.github.com/login'
r2=session.get(login_url,headers=headers)
html=r2.content.decode('utf-8')
cookies=r2.cookies.get_dict()

pattern_timestamp=re.compile('<input type="hidden" name="timestamp" value="(.*?)" class="form-control" />')
timestamp=pattern_timestamp.findall(html)[0]
print('timestamp:',timestamp)
pattern_timestamp_secret=re.compile('<input type="hidden" name="timestamp_secret" value="(.*)" class="form-control" />')
timestamp_secret=pattern_timestamp_secret.findall(html)[0]
print('timestamp_secret:',timestamp_secret)
session_url='https://github.com/session'
data={
    'commit':'Sign+in',
    'authenticity_token':auth_token,
    'login':'username',#
    'password':'password',#
    'webauthn-support':'supported',
    'webauthn-iuvpaa-support': 'supported',
    'timestamp':timestamp,
    'timestamp_secret':timestamp_secret,

}
headers['referer']='https://github.com/login'
headers['origin']='https://github.com'
r3=session.post(session_url,data=data,headers=headers,cookies=cookies)
print(r3.status_code)
#print(r3.content.decode('utf-8'))

