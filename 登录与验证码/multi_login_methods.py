import requests
from login_github_by_cookies import is_login
from github_login import parse_and_login
'''兼容cookies登录与post登录'''

def login(username,password):
    parse_and_login(username,password)

if __name__=='__main__':
    if is_login():
        print('已登录')
    else:
        username="username"#
        password="password"#
        login(username,password)