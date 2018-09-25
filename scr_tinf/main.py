#! /usr/bin/env python
'''
Created on 2018年7月29日

@author: 54564
'''

import requests
from address_scraper import scr_all
from getpass import getpass


#初始化
s=requests.Session()
formdata={}
formdata['username']=input('username:')
formdata['password']=getpass('password:')

#访问综合服务平台，取得cookies
url='http://uis.shou.edu.cn/cas/login?isLoginService=11&service=http://ecampus.shou.edu.cn/c/portal/login'
r=s.post(url,formdata)
print(s.cookies)
# print(r.text)

#带着cookies访问通讯录
scr_all(s)

#退出
s.close()
