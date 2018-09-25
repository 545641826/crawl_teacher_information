#! /usr/bin/env python
'''
Created on 2018年7月29日

@author: 54564
'''
from cutter import cut
import requests
from address_scraper import scr_all



#初始化
formdata=cut('formdata') 
s=requests.Session()

#访问综合服务平台，取得cookies
url='http://uis.shou.edu.cn/cas/login?isLoginService=11&service=http://ecampus.shou.edu.cn/c/portal/login'
s.post(url,formdata)

#带着cookies访问通讯录
scr_all(s)

#退出
s.close()



